from DataGetter import DataGetter
from DepthMeasurer import DepthMeasurer

def main():
    dataGetter = DataGetter()
    data = dataGetter.get_data()
    depth_measurer = DepthMeasurer()
    depth_measurer.set_measures(data)
    print('Part 1: Number of increases: ', depth_measurer.increases_counter())
    print('Part 2: Number of increases with windows: ', depth_measurer.increases_in_windows_of_three())

if __name__ == "__main__":
    main()

