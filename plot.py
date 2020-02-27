#!/usr/bin/python3
import matplotlib.pyplot as plt
import csv

def load(filename):
    freq = []
    amp = []
    count = 0
    with open(filename) as fh:
        reader = csv.reader(fh)
        for row in reader:
            freq.append(float(row[0]))
            amp.append(float(row[1]))

    return freq, amp

def plot(freq, amp):
    fig, ax = plt.subplots()

    # freq plot
    ax.set(xlabel='Freq (kHz)', ylabel='Amp (V)', title='frequency response')
    ax.set(xlim=(0, 2000000), ylim=(0, 6))
    ax.grid(True)
    ax.plot(freq, amp)

    plt.show()

if __name__ == '__main__':
    freq, amp = load("results.csv")
    plot(freq, amp)

