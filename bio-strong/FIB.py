def rabbits(months, offspring):
    if months == 1:
        return 1
    if months == 2:
        return 1
    return rabbits(months - 1, offspring) + rabbits(months - 2, offspring) * offspring
