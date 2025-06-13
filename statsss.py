##statistics module#
import statistics as s
print(s.mean([1, 2, 3, 4, 5]))                   # mean
print(s.median([1, 2, 3, 4, 5]))                 # median
print(s.mode([1, 2, 2, 3, 4]))                   # mode
print(s.stdev([1, 2, 3, 4, 5]))                  # standard deviation
print(s.variance([1, 2, 3, 4, 5]))               # variance
print(s.pstdev([1, 2, 3, 4, 5]))                 # population standard deviation
print(s.pvariance([1, 2, 3, 4, 5]))              # population variance
print(s.quantiles([1, 2, 3, 4, 5], n=4))        # quantiles
print(s.median_low([1, 2, 3, 4, 5]))            # median low
print(s.median_high([1, 2, 3, 4, 5]))           # median high
print(s.median_grouped([1, 2, 3, 4, 5], interval=1))  # median grouped
print(s.geometric_mean([1, 2, 3, 4, 5]))        # geometric mean
print(s.harmonic_mean([1, 2, 3, 4, 5]))         # harmonic mean
print(s.fmean([1, 2, 3, 4, 5]))                  # floating point mean
print(s.multimode([1, 2, 2, 3, 4]))              # multimode
print(s.NormalDist(mu=0, sigma=1).mean)          # normal distribution mean
print(s.NormalDist(mu=0, sigma=1).stdev)         # normal distribution standard deviation
print(s.NormalDist(mu=0, sigma=1).variance)      # normal distribution variance
print(s.NormalDist(mu=0, sigma=1).cdf(1))        # cumulative distribution function
print(s.NormalDist(mu=0, sigma=1).pdf(1))        # probability density function
print(s.NormalDist(mu=0, sigma=1).inv_cdf(0.8413))  # inverse cumulative distribution function
print(s.NormalDist(mu=0, sigma=1).samples(10))  # generate samples from normal distribution
print(s.NormalDist(mu=0, sigma=1).samples(10, seed=42))  # generate samples with seed
print(s.NormalDist(mu=0, sigma=1).zscore(1))     # z-score


