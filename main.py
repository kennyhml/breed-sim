from logging import config
import configs
from stats import Stats
import random


def rolled_mutation() -> bool:
    male_chosen = random.choice([True, False])

    if (male_chosen and not configs.MALE_SUB_20_MUTATIONS) or (
        not male_chosen and not configs.FEMALES_SUB_20_MUTATIONS
    ):
        return False

    return random.uniform(0, 1) < 0.025

def main():
    got_mutation_times = 0

    for _ in range(configs.NUM_SIMULATIONS):
        muta_got = False
        mutations_got = 0
        for female in range(configs.NUM_FEMALES):
            # mutations roll 3 times
            for reroll in range(3):
                if not rolled_mutation():
                    continue
                
                mutations_got += 1
                # a mutation was rolled, roll into a stat
                rolled_stat = random.randrange(0, configs.NUM_SELECTABLE_STATS)
                if (
                    rolled_stat == configs.DESIRED_STAT.value
                    and random.uniform(0, 1) < 0.55 and random.uniform(0, 1) < 0.50
                ):
                    if not muta_got:
                        got_mutation_times += 1
                    muta_got = True

    print(got_mutation_times)


if __name__ == "__main__":
    main()
