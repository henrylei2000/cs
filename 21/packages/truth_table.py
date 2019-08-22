def truth_table(expression):
    print(" any_other_point   q   %s" % (expression))
    length = len(" any_other_point   q   %s" % (expression))
    print(length*"=")

    for p in True, False:
        for q in True, False:
            print("%7s %7s %7s" % (p, q, eval(expression))) # no hyphen between % and 7
