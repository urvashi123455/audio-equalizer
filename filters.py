from scipy.signal import butter, lfilter

# LOW PASS FILTER
def low_pass_filter(data, cutoff, fs, order=5):

    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist

    b, a = butter(order, normal_cutoff, btype='low')

    filtered_data = lfilter(b, a, data)

    return filtered_data


# HIGH PASS FILTER
def high_pass_filter(data, cutoff, fs, order=5):

    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist

    b, a = butter(order, normal_cutoff, btype='high')

    filtered_data = lfilter(b, a, data)

    return filtered_data


# BAND PASS FILTER
def band_pass_filter(data, lowcut, highcut, fs, order=5):

    nyquist = 0.5 * fs

    low = lowcut / nyquist
    high = highcut / nyquist

    b, a = butter(order, [low, high], btype='band')

    filtered_data = lfilter(b, a, data)

    return filtered_data