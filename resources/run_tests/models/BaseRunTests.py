from dataclasses import dataclass
import numpy as np

@dataclass
class BaseRunTests:
    number_of_rounds : int = 180 # days
    number_of_options : int = 60
    cycled_events_each_week_percentage : float = 0.2
    daily_access : int = 1_000
    conversion_percentage : float = 0.1
    rank_bandit_instance : None
    model_type : None

    def __post_init__(self):
        pass

    def _initialize_options_true_conversion(self):
        pass

    def _cycle_percentage_of_options(self):
        pass

    def 