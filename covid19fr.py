#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from astropy.modeling import models, fitting
import matplotlib.pyplot as plt

## Data
day = np.arange(16) + 2
print(day)
case = np.array((3,13,18,38,57,100,130,191,212,285,423,613,949,1126,1412,1784))+500
xday = np.arange(len(day)+7) + 2

## Choose a model
print('Available models: lin, poly, exp, power')
model = input('Choose a model: ')

## Init fitters and models
fit = fitting.LevMarLSQFitter()

mod_off = models.Shift()
mod_lin = models.Linear1D()
mod_poly = models.Polynomial1D(degree=2)
mod_exp = models.Exponential1D()

## Fit
if model=='lin':
    mod = mod_lin
elif model=='poly':
    mod = mod_poly
elif model=='exp':
    mod = mod_exp + mod_off

if model=='power':
    mod = mod_lin
    yoff = float(input('Enter offset: '))
    x = np.log(day)
    y = np.log(case-yoff)
else:
    x = day
    y = case

fitted = fit(mod, x, y)
print(model)
print(fitted)
if model=='power':
    predict = np.exp(fitted(np.log(xday))) + yoff
else:
    predict = fitted(xday)

## Plot
plt.figure()
plt.plot(day, case, 'ko', label='Data')
plt.plot(xday, predict, 'b-', label='Prediction')
plt.xlabel('Days')
plt.ylabel('Cases')
plt.show()
