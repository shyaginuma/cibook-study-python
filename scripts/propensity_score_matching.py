import pandas as pd

class PropensityScoreMatching:
    def __init__(self, treatment, control, pscore_col='pscore'):
        self.treatment = treatment
        self.control = control
        self.pscore_col = pscore_col
        self.match_idx = {}

    def match(self):
        threshold = pd.concat([self.treatment, self.control])[self.pscore_col].std() * 0.2  # see: https://www.slideshare.net/okumurayasuyuki/ss-43780294
        match_pair_df = self.control.copy(deep=True)
        for i in range(self.treatment.shape[0]):
            matching_target = self.treatment.loc[i, self.pscore_col]
            matched_pair = ((match_pair_df[self.pscore_col] - matching_target)**2).loc[lambda x: x < threshold]
            if matched_pair.shape[0] != 0:  # マッチング対象が存在する場合
                matched_pair = matched_pair.idxmin()
                self.match_idx[i] = matched_pair

                if i % 5000 == 1:
                    print('Matching : [{}]. Propensity Score: {} Matched : [{}]. Propensity Score: {}'.format(
                        i, matching_target, matched_pair, match_pair_df.loc[matched_pair, self.pscore_col]
                    ))

                match_pair_df = match_pair_df.drop(matched_pair)
        print("Matched Ratio: {}".format(len(self.match_idx.keys())/self.treatment.shape[0]))

    def create_matched_df(self, target_col):
        if len(self.match_idx.keys()) == 0:
            raise AttributeError("マッチングが行われていません。match()を呼び出した後に使ってください。")

        columns = ['idx', 'pscore', target_col, 'matched_idx', 'matched_pscore', 'matched_{}'.format(target_col)]
        idx, pscore, target, matched_idx, matched_pscore, matched_target = [], [], [], [], [], []
        for i, v in self.match_idx.items():
            idx += [i]
            pscore += [self.treatment.loc[i, self.pscore_col]]
            target += [self.treatment.loc[i, target_col]]
            matched_idx += [v]
            matched_pscore += [self.control.loc[v, self.pscore_col]]
            matched_target += [self.control.loc[v, target_col]]

        matched_df = pd.DataFrame(data = {col: val for col, val in zip(columns, [idx, pscore, target, matched_idx, matched_pscore, matched_target])})
        matched_df['diff'] = matched_df[target_col] - matched_df['matched_{}'.format(target_col)]
        return matched_df