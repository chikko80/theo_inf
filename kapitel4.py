def main():
    print(calc_rel_error(3, 2, min_prob=False))
    print(calc_rel_error(3, 2, min_prob=True))



def calc_rel_error(erg_apx, opt, min_prob=False):
    if min_prob:
        return (erg_apx / opt) - 1
    else:
        return (1 / (opt / erg_apx)) - 1


if __name__ == "__main__":
    main()
