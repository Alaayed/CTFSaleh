from enum import Enum
import math
x1,x2,x3,x4= 1, 3, 7, 11
w1, w2 = 1/2, 1/2
mu1,mu2 = 4, 8
sigma1,sigma2 = 1, 1
allx = [x1,x2,x3,x4]
gammas = []
weights = [w1, w2]
sigmas = [sigma1, sigma2]
means = [mu1, mu2]
def guassian(x, mu, sigma):
    return math.exp(-(x-mu)**2/(2*sigma**2)) / math.sqrt(2*math.pi*sigma**2)
for x in allx:
    denominator = w1*guassian(x, mu1, sigma1) + w2*guassian(x, mu2, sigma2)
    numerator = w1 * guassian(x, mu1, sigma1)
    gamma1 = numerator / denominator
    gamma2 = 1 - gamma1
    gammas.append((gamma1, gamma2))
# Compute Updated Weights
for i, w in enumerate(weights):
    new_w = 0
    n = len(allx)
    for j, x in enumerate(allx):
        gamma_of_x = gammas[j][i]
        new_w += gamma_of_x
    new_w /= n
    weights[i] = new_w
new_means = []
# Compute Updated Means
for i, mu in enumerate(means):
    new_mu = 0
    n = len(allx)
    for j, x in enumerate(allx):
        gamma_of_x = gammas[j][i]
        new_mu += gamma_of_x * x
    w_k = weights[i]
    new_mu /= (w_k * n)
    new_means.append(new_mu)
# Compute Updated Sigmas
for i, sigma in enumerate(sigmas):
    new_sigma = 0
    n = len(allx)
    for j, x in enumerate(allx):
        gamma_of_x = gammas[j][i]
        new_sigma += gamma_of_x * (x - new_means[i])**2
    w_k = weights[i]
    new_sigma /= (w_k * n)
    sigmas[i] = new_sigma
print(f'Updated means: mu1: {new_means[0]:.5f} , mu2: {new_means[1]:.5f}')
print(f'Updated weights: w1: {weights[0]:.5f} , w2: {weights[1]:.5f}')
print(f'Updated sigmas: sigma1: {sigmas[0]:.5f} , sigma2: {sigmas[1]:.5f}')
