#!/usr/bin/env bash
gcc $1.c -o $1 -lm
./$1
