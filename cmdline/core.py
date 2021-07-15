try:
    import sys
    import gettext
    from gettext import gettext as _
    gettext.textdomain('cmdline')

    from progressbar import ProgressBar
    from progressbar import FormatLabel
    from progressbar import Percentage
    from progressbar import Bar
    from progressbar import RotatingMarker
    from progressbar import ETA
    import time

except ImportError as err:
    modulename = err.args[0].partition("'")[-1].rpartition("'")[0]
    print(_("No fue posible importar el modulo: %s") % modulename)
    sys.exit(-1)

def sum_function_to_test(a, b):
    return a+b

def main():

    print("Executing main")

    f = 1
    t = 10
    widgets = [FormatLabel(''), ' ', Percentage(), ' ', Bar('#'), ' ', ETA(), ' ', RotatingMarker()]
    bar = ProgressBar(widgets=widgets, maxval=t)

    for i in range(1, t+1):
        widgets[0] = FormatLabel('[Contador: {0}]'.format(i))
        time.sleep(1)
        bar.update(i)

    bar.finish()

if __name__ == "__main__":

	main()