from dataclasses import dataclass
import numpy as np
from BaseRunTests import BaseRunTests

@dataclass
class RunTests(BaseRunTests):
    number_of_rounds : int = 180 # days
    number_of_options : int = 60
    cycled_events_each_week_percentage : float = 0.2
    daily_visits : int = 1_000
    rank_bandit_instance : None
    model_type : None

    def __post_init__(self):
        self.options_true_probs = self._initialize_options_true_probs_of_converting()

    def _initialize_options_true_probs_of_converting(self):
        # define here terms from 0.005 ~ 0.025
        lower_bound = 0.005
        upper_bound = 0.025
        return np.random.uniform(lower_bound, upper_bound, self.number_of_options)

    def run_tests(self):
        for i in range(0, self.number_of_rounds):
            array_of_chosen_lists_of_options = self._choose_for_n_users()
            # for each, sort a chosen option (or not) - kinda hard!
            self._update_model()
            # after n rounds, cycle some options

    def see_results(self):
        pass

    # Not priority atm
    def _cycle_percentage_of_options(self):
        pass

    def _choose_for_n_users(self):
        pass

    def _update_model(self):
        pass

    def _plot_(self):
        pass