create database Coal_price_analysis;
use coal_price_analysis;
select * from coal_ore;


-- EDA(EXPLORATORY DATA ANALYSIS):
-- 1ST MOMENT BUSINESS DECISION:
-- MEAN:
select avg(open) as mean_open,
       avg(High) as mean_high,
       avg(low) as mean_low,
       avg(`Close`) as mean_close,
       avg(`Trend Supertrend (7,3)`) as mean_Trend_Supertrend,
       avg(`MACD (12,26,9)`) as mean_MACD,
       avg(`Signal MACD (12,26,9)`) as mean_Signal_MACD,
       avg(`MACD (12,26,9)_hist`) as mean_MACD_hist,
       avg(volume) as mean_valume 
       from coal_ore;
-- output:
-- mean_open_price: 185.42566316793918	
-- mean_high_price: 193.57744274809139	
-- mean_low_price: 178.9528244274806	
-- mean_close_price: 186.27328721374067
-- mean_Trend_Supertrend:175.74745229007635
-- mean_MACD:2.265162213740456
-- mean_Signal_MACD:1.8045419847328277
-- mean_MACD_hist:0.8110973282442749
-- mean_valume:55730747.4580

-- MEDIAN:
with CTE as
(select open,row_number() over (order by open) as row_num,
count(*) over() as total_count
from coal_ore)
select round(avg(open),3) as median_open 
from cte
where row_num in (floor((total_count+1)/2),ceil((total_count+1)/2));
-- median_open_price: 177.595

with CTE as
(select High,row_number() over (order by High) as row_num,
count(*) over() as total_count
from coal_ore)
select round(avg(High),3) as median_High
from cte
where row_num in (floor((total_count+1)/2),ceil((total_count+1)/2));
-- median_high_price:186.825

with cte as(
select Low,row_number() over (order by Low) as row_num,
count(*) over () as total_count
from coal_ore)
select round(avg(Low),3) as median_Low
from cte
where row_num in (floor((total_count+1)/2),ceil((total_count+1)/2));
-- median_low_price: 169.2

with CTE as
(select Close,row_number() over (order by Close) as row_num,
count(*) over() as total_count
from coal_ore)
select round(avg(Close),3) as median_Close 
from cte
where row_num in (floor((total_count+1)/2),ceil((total_count+1)/2));
-- median_close_price :177.12


with CTE as
(select `Trend Supertrend (7,3)`,row_number() over (order by `Trend Supertrend (7,3)`) as row_num,
count(*) over() as total_count
from coal_ore)
select round(avg(`Trend Supertrend (7,3)`),3) as `median_Trend_Supertrend_(7,3)`
from cte
where row_num in (floor((total_count+1)/2),ceil((total_count+1)/2));
-- median_Trend_Supertrend_(7,3): 181.985

with CTE as
(select `MACD (12,26,9)`,row_number() over (order by `MACD (12,26,9)`) as row_num,
count(*) over() as total_count
from coal_ore)
select round(avg(`MACD (12,26,9)`),3) as `median_MACD (12,26,9)`
from cte
where row_num in (floor((total_count+1)/2),ceil((total_count+1)/2));
-- median_MACD (12,26,9):1.945

with CTE as
(select `Signal MACD (12,26,9)`,row_number() over (order by `Signal MACD (12,26,9)`) as row_num,
count(*) over() as total_count
from coal_ore)
select round(avg(`Signal MACD (12,26,9)`),3) as `median_Signal MACD (12,26,9)`
from cte
where row_num in (floor((total_count+1)/2),ceil((total_count+1)/2));
-- median_Signal MACD (12,26,9)`:2.055

with CTE as
(select `MACD (12,26,9)_hist`,row_number() over (order by `MACD (12,26,9)_hist`) as row_num,
count(*) over() as total_count
from coal_ore)
select round(avg(`MACD (12,26,9)_hist`),3) as `median_MACD (12,26,9)_hist`
from cte
where row_num in (floor((total_count+1)/2),ceil((total_count+1)/2));
-- median_MACD (12,26,9)_hist:0.865

with CTE as
(select volume,row_number() over (order by volume) as row_num,
count(*) over() as total_count
from coal_ore)
select round(avg(volume),3) as median_volume 
from cte
where row_num in (floor((total_count+1)/2),ceil((total_count+1)/2));
-- median_volume: 50226774.500

-- second moment of bussiness understanding(measure of dispersion):
-- variance:
select variance(open) as variance_open,
	   variance(high) as variance_high,
       variance(low) as variance_low,
       variance(close) as variance_close,
       variance(`Trend Supertrend (7,3)`) as `variance_Trend_Supertrend_(7,3)`,
       variance(`MACD (12,26,9)`) as `variance_MACD_(12,26,9)`,
       variance(`Signal MACD (12,26,9)`) as `variance_Signal_MACD_(12,26,9)`,
       variance(`MACD (12,26,9)_hist`) as `variance_MACD (12,26,9)_hist`,
       variance(volume) as variance_volume
       from coal_ore;
						
 -- variance_open:4006.4772695089223	
 -- variance_high:4267.230163307783	
 -- variance_low:4129.921916259253	
 -- variance_close:4196.876223610973	
 -- variance_Trend_Supertrend_(7,3):3580.7467107086027
 -- variance_MACD_(12,26,9):125.33778587540425
 -- variance_Signal_MACD_(12,26,9):115.122224790222
 -- variance_MACD (12,26,9)_hist:8.297236272015764
 -- variance_volume:765064076174047.9    
 
 -- standard deviation:
 select stddev(open) as stddev_open,
	   stddev(high) as stddev_high,
       stddev(low) as stddev_low,
       stddev(close) as stddev_close,
       stddev(`Trend Supertrend (7,3)`) as `stddev_Trend_Supertrend_(7,3)`,
       stddev(`MACD (12,26,9)`) as `stddev_MACD (12,26,9)`,
       stddev(`Signal MACD (12,26,9)`) as `stddev_Signal MACD (12,26,9)`,
       stddev(`MACD (12,26,9)_hist`) as `MACD (12,26,9)_hist`,
       stddev(volume) as stddev_volume
       from coal_ore;
-- stddev_open:63.29673980158		
-- stddev_high: 65.32403970444405	
-- stddev_low:64.26446853634792	
-- stddev_close:64.78330204312661	
-- stddev_Trend_Supertrend_(7,3):59.83934082782499	
-- stddev_MACD (12,26,9):11.195435939498035
-- stddev_Signal MACD (12,26,9):10.729502541600985
-- MACD (12,26,9)_hist:2.8804923662484794
-- stddev_volume:27659791.68710509

-- range:
select max(open)-min(open) as range_open,
       max(high)-min(high) as range_high,
       max(low)-min(low) as range_low,
       max(close)-min(close) as range_close,
       max(`Trend Supertrend (7,3)`)-min(`Trend Supertrend (7,3)`) as `range_Trend Supertrend (7,3)`,
       max(`MACD (12,26,9)`)-min(`MACD (12,26,9)`) as `range_MACD (12,26,9)`,
       max(`Signal MACD (12,26,9)`)-min(`Signal MACD (12,26,9)`) as `range_Signal MACD (12,26,9)`,
       max(`MACD (12,26,9)_hist`)-min(`MACD (12,26,9)_hist`) as `range_MACD (12,26,9)_hist`,
       max(volume)-min(volume) as range_volume
       from coal_ore;						
-- range_open:245.08375	
-- range_high:248.79999999999998	
-- range_low:246.27499999999998	
-- range_close:246.53375	
-- range_Trend Supertrend (7,3): 234.2525
-- range_MACD (12,26,9): 45.712500000000006
-- range_Signal MACD (12,26,9): 44.81999999999999 
-- range_MACD (12,26,9)_hist: 13.622499999999999
-- range_volume:112794512

-- third moment of bussiness understanding:
-- skewness:
select round(sum(power(open-(select avg(open) from coal_ore),3))/
       count(open)/power((select stddev(open) from coal_ore),3),3) as skewness_open,
       round(sum(power(high-(select avg(high) from coal_ore),3))/
       count(high)/power((select stddev(high) from coal_ore),3),3) as skewness_high,
       round(sum(power(low-(select avg(low) from coal_ore),3))/
       count(low)/power((select stddev(low) from coal_ore),3),3) as skewness_low,
       round(sum(power(close-(select avg(close) from coal_ore),3))/
       count(close)/power((select stddev(close) from coal_ore),3),3) as skewness_close,
       round(sum(power(`Trend Supertrend (7,3)`-(select avg(`Trend Supertrend (7,3)`) from coal_ore),3))/
       count(`Trend Supertrend (7,3)`)/power((select stddev(`Trend Supertrend (7,3)`) from coal_ore),3),3) as `skewness_Trend Supertrend (7,3)`,
       round(sum(power(`MACD (12,26,9)`-(select avg(`MACD (12,26,9)`) from coal_ore),3))/
       count(`MACD (12,26,9)`)/power((select stddev(`MACD (12,26,9)`) from coal_ore),3),3) as `skewness_MACD (12,26,9)`,
       round(sum(power(`Signal MACD (12,26,9)`-(select avg(`Signal MACD (12,26,9)`) from coal_ore),3))/
       count(`Signal MACD (12,26,9)`)/power((select stddev(`Signal MACD (12,26,9)`) from coal_ore),3),3) as `skewness_Signal MACD (12,26,9)`,
       round(sum(power(`MACD (12,26,9)_hist`-(select avg(`MACD (12,26,9)_hist`) from coal_ore),3))/
       count(`MACD (12,26,9)_hist`)/power((select stddev(`MACD (12,26,9)_hist`) from coal_ore),3),3) as `skewness_MACD (12,26,9)_hist`,
       round(sum(power(volume-(select avg(volume) from coal_ore),3))/
       count(volume)/power((select stddev(volume) from coal_ore),3),3) as skewness_volume
       from coal_ore;
								
-- skewness_open_price:1.022	
-- skewness_high_price:0.975	
-- skewness_low_price:1.06
-- skewness_close_price:1.004	
-- skewness_Trend Supertrend (7,3):0.717	
-- skewness_MACD (12,26,9):0.495
-- skewness_Signal MACD (12,26,9):0.616	
-- skewness_MACD (12,26,9)_hist:0.166	
-- skewness_volume:0.877

-- kurtosis:
select sum(power(open-(select avg(open) from coal_ore),4))/
       count(open)/power((select stddev(open) from coal_ore),4)-3 as kurt_open,
       (sum(power(high-(select avg(high) from coal_ore),4))/
       count(high)/(power((select stddev(high) from coal_ore),4))-3)  as kurt_high ,
       (sum(power(low-(select avg(low) from coal_ore),4))/
       count(low)/(power((select stddev(low) from coal_ore),4))-3)  as kurt_low,
       (sum(power(close-(select avg(close) from coal_ore),4))/
       count(close)/(power((select stddev(close) from coal_ore),4))-3)  as kurt_close,
       (sum(power(`Trend Supertrend (7,3)`-(select avg(`Trend Supertrend (7,3)`) from coal_ore),4))/
       count(`Trend Supertrend (7,3)`)/(power((select stddev(`Trend Supertrend (7,3)`) from coal_ore),4))-3)  as `kurt_Trend Supertrend (7,3)`,
       (sum(power(`MACD (12,26,9)`-(select avg(`MACD (12,26,9)`) from coal_ore),4))/
       count(`MACD (12,26,9)`)/(power((select stddev(`MACD (12,26,9)`) from coal_ore),4))-3)  as `kurt_MACD (12,26,9)`,
	   (sum(power(`Signal MACD (12,26,9)`-(select avg(`Signal MACD (12,26,9)`) from coal_ore),4))/
       count(`Signal MACD (12,26,9)`)/(power((select stddev(`Signal MACD (12,26,9)`) from coal_ore),4))-3)  as `kurt_Signal MACD (12,26,9)`,
       (sum(power(`MACD (12,26,9)_hist`-(select avg(`MACD (12,26,9)_hist`) from coal_ore),4))/
       count(`MACD (12,26,9)_hist`)/(power((select stddev(`MACD (12,26,9)_hist`) from coal_ore),4))-3)  as `kurt_MACD (12,26,9)_hist`,
       (sum(power(volume-(select avg(volume) from coal_ore),4))/
       count(volume)/(power((select stddev(volume) from coal_ore),4))-3)  as kurt_volume
       from coal_ore;
       				
  --  kurt_open_price:0.6181765939495953	
  -- kurt_high_price:0.4356397744626066
  -- kurt_low_price:0.6391713559262344
  -- kurt_close_price:0.4809270804790473	
  -- kurt_Trend Supertrend (7,3):0.06826968479747153
  -- kurt_MACD (12,26,9):0.08602169979489593
  -- kurt_Signal MACD (12,26,9):0.33209393152807865
  -- kurt_MACD (12,26,9)_hist:0.01234892647626129
  -- kurt_volume:0.1494235778217412    
