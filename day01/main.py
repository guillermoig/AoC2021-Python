from DataGetter import DataGetter
from DepthMeasurer import DepthMeasurer

def main():
    dataGetter = DataGetter()
    data = dataGetter.get_data()
    depth_measurer = DepthMeasurer()
    depth_measurer.set_measures(data)
    print('Number of increases: ', depth_measurer.increases_counter())

if __name__ == "__main__":
    main()

