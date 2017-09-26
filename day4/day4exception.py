def section1():
    while True:
        amount = raw_input("Enter the amount to withdraw")

        try:
            amount = int(amount)
            print "Collect cash"
            break
        # get the exception as an object
        except ValueError as e:
            print "Enter a valid number"
            print "The exception that occured was -", e
            print type(e)
            print dir(e)
            print e.args
            print e.message


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print "division by zero!"
    except TypeError:
        print "Wrong data type. Use integer"
    # catch all possible exceptions
    except Exception:
        print "Something happened"
    # Not recommended at all. Too broad
    except:
        print "whaaaaaa"
    # else gets executed if try is run successfully
    else:
        print "Result is", result
    # finally is always executed
    finally:
        print "Executing finally clause"


def section2():
    divide(2, 1)
    divide(2, 0)
    divide('a', 'b')

    print "done"

# create custom exceptions
# another function can handle the exception
def section3():
    import time, random

    def get_temp():
        return random.randint(20, 120)

    OverHeatError = Exception("Engine temp beyond normal")

    while True:
        cartemp = get_temp()
        print cartemp
        if cartemp > 115:
            raise OverHeatError
        time.sleep(1)


# assert a condition, loop continues if the condition is true
# more readable
def section4():
    marks = [45, 78, 69, 23, 90, 12, 56, 89]

    for x in marks:
        print x
        assert x > 35


# In python it's easier to get pardon than permission
# handle exception when it occurs instead of looking for stuff

# section1()
# section2()
# section3()
section4()
