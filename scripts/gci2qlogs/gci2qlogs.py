#!/usr/bin/env python

import argparse, os, re, struct, sys

def main():
    parser = argparse.ArgumentParser(description="Parses out quest logs from a The Wind Waker GCI")
    parser.add_argument("gci", help="A valid wind waker GCI file")
    gcibytes = None
    args = parser.parse_args()
    file_in = args.gci
    with open(file_in,"rb") as gcifile:
        gcibytes = bytearray(gcifile.read())
    
    qlog1 = gcibytes[0x4048:0x47B8]
    qlog2 = gcibytes[0x47B8:0x4F28]
    qlog3 = gcibytes[0x4F28:0x5698]

    with open("qlog1.bin", "wb") as outfile:
        outfile.write(qlog1)

    with open("qlog2.bin", "wb") as outfile:
        outfile.write(qlog2)

    with open("qlog3.bin", "wb") as outfile:
        outfile.write(qlog3)
    
if __name__ == "__main__":
    main()