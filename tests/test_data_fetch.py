import sys
sys.path.insert(0,'../scripts/')
from scripts.data_fetch import get_data

def test_data_fetch():
    driver_location_data = get_data('data/driver_locations_during_request.csv','C:/Users/User/Desktop/Causal-Inference','driver_locations_during_request_v1')
    nb_data = get_data('data/nb.csv','C:/Users/User/Desktop/Causal-Inference','nb_v1')
    assert driver_location_data.shape[0] == 1557740
    assert nb_data.shape[0] == 536020