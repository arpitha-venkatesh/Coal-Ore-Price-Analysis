-- pre-procesing 
use coal_price_analysis;
select * from coal_ore;
select count(*) from coal_ore;
-- 262

-- typecasting:
set sql_safe_updates=0;
UPDATE coal_ore SET date = STR_TO_DATE(date, '%d-%m-%Y');
alter table coal_ore modify column date date;


-- duplication handling:
select date,open,high,low,close,`Trend Supertrend (7,3)`,`MACD (12,26,9)`,`Signal MACD (12,26,9)`,`MACD (12,26,9)_hist`,Volume,count(*) as num_duplicates
from coal_ore
group by date,open,high,low,close,`Trend Supertrend (7,3)`,`MACD (12,26,9)`,`Signal MACD (12,26,9)`,`MACD (12,26,9)_hist`,Volume
having count(*)>1;
-- there is no duplicated records

-- missing values:
select 
sum(case when date is null then 1 else 0 end) as date_null_count,
sum(case when open is null then 1 else 0 end) as open_null_count,
sum(case when high is null then 1 else 0 end) as high_null_count,
sum(case when close is null then 1 else 0 end) as close_null_count,
sum(case when `Trend Supertrend (7,3)` is null then 1 else 0 end) as `Trend Supertrend (7,3)_null_count`,
sum(case when `MACD (12,26,9)` is null then 1 else 0 end) as `MACD (12,26,9)_null_count`,
sum(case when `Signal MACD (12,26,9)` is null then 1 else 0 end) as `Signal MACD (12,26,9)_null_count`,
sum(case when `MACD (12,26,9)_hist` is null then 1 else 0 end) as `MACD (12,26,9)_hist_null_count`,
sum(case when volume is null then 1 else 0 end) as volume_null_count
from coal_ore;
-- output:
-- date_null_count:0
-- open_null_count:0
-- high_null_count:0
-- close_null_count:0
-- Trend Supertrend (7,3)_null_count:0
-- MACD (12,26,9)_null_count:0
-- Signal MACD (12,26,9)_null_count:0
-- MACD (12,26,9)_hist_null_count:0
-- volume_null_count:0

-- zero variance :
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

-- outliers:
-- finding outliers outliers
with outliers as(
select open,row_number() over (order by open) as row_n
from coal_ore),
iqr as 
(select open,
q3_value as q_three,
q1_value as q_one,
q3_value-q1_value as outlier_range
from outliers
join(select open as q3_value from outliers where row_n=floor((select count(*) from coal_ore)*0.75))q3 on 1=1
join (select open as q1_value from outliers where row_n=floor((select count(*) from coal_ore)*0.75))q1 on 1=1
)
select open as outliers_value
from iqr
where open>=q_three+outlier_range
or open<=q_one-outlier_range;

with outliers as(
select High,row_number() over (order by High) as row_n
from coal_ore),
iqr as 
(select High,
q3_value as q_three,
q1_value as q_one,
q3_value-q1_value as outlier_range
from outliers
join(select High as q3_value from outliers where row_n=floor((select count(*) from coal_ore)*0.75))q3 on 1=1
join (select High as q1_value from outliers where row_n=floor((select count(*) from coal_ore)*0.75))q1 on 1=1
)
select High as outliers_value
from iqr
where High>=q_three+outlier_range
or High<=q_one-outlier_range;

with outliers as(
select Low,row_number() over (order by Low) as row_n
from coal_ore),
iqr as 
(select Low,
q3_value as q_three,
q1_value as q_one,
q3_value-q1_value as outlier_range
from outliers
join(select Low as q3_value from outliers where row_n=floor((select count(*) from coal_ore)*0.75))q3 on 1=1
join (select Low as q1_value from outliers where row_n=floor((select count(*) from coal_ore)*0.75))q1 on 1=1
)
select Low as outliers_value
from iqr
where Low>=q_three+outlier_range
or Low<=q_one-outlier_range;

with outliers as(
select Close,row_number() over (order by Close) as row_n
from coal_ore),
iqr as 
(select Close,
q3_value as q_three,
q1_value as q_one,
q3_value-q1_value as outlier_range
from outliers
join(select Close as q3_value from outliers where row_n=floor((select count(*) from coal_ore)*0.75))q3 on 1=1
join (select Close as q1_value from outliers where row_n=floor((select count(*) from coal_ore)*0.75))q1 on 1=1
)
select Close as outliers_value
from iqr
where Close>=q_three+outlier_range
or Close<=q_one-outlier_range;


with outliers as(
select `Trend Supertrend (7,3)`,row_number() over (order by `Trend Supertrend (7,3)`) as row_n
from coal_ore),
iqr as 
(select `Trend Supertrend (7,3)`,
q3_value as q_three,
q1_value as q_one,
q3_value-q1_value as outlier_range
from outliers
join(select `Trend Supertrend (7,3)` as q3_value from outliers where row_n=floor((select count(*) from coal_ore)*0.75))q3 on 1=1
join (select `Trend Supertrend (7,3)` as q1_value from outliers where row_n=floor((select count(*) from coal_ore)*0.75))q1 on 1=1
)
select `Trend Supertrend (7,3)` as outliers_value
from iqr
where `Trend Supertrend (7,3)`>=q_three+outlier_range
or `Trend Supertrend (7,3)`<=q_one-outlier_range;

with outliers as(
select `MACD (12,26,9)`,row_number() over (order by `MACD (12,26,9)`) as row_n
from coal_ore),
iqr as 
(select `MACD (12,26,9)`,
q3_value as q_three,
q1_value as q_one,
q3_value-q1_value as outlier_range
from outliers
join(select `MACD (12,26,9)` as q3_value from outliers where row_n=floor((select count(*) from coal_ore)*0.75))q3 on 1=1
join (select `MACD (12,26,9)` as q1_value from outliers where row_n=floor((select count(*) from coal_ore)*0.75))q1 on 1=1
)
select `MACD (12,26,9)` as outliers_value
from iqr
where `MACD (12,26,9)`>=q_three+outlier_range
or `MACD (12,26,9)`<=q_one-outlier_range;

with outliers as(
select `Signal MACD (12,26,9)`,row_number() over (order by `Signal MACD (12,26,9)`) as row_n
from coal_ore),
iqr as 
(select `Signal MACD (12,26,9)`,
q3_value as q_three,
q1_value as q_one,
q3_value-q1_value as outlier_range
from outliers
join(select `Signal MACD (12,26,9)` as q3_value from outliers where row_n=floor((select count(*) from coal_ore)*0.75))q3 on 1=1
join (select `Signal MACD (12,26,9)` as q1_value from outliers where row_n=floor((select count(*) from coal_ore)*0.75))q1 on 1=1
)
select `Signal MACD (12,26,9)` as outliers_value
from iqr
where `Signal MACD (12,26,9)`>=q_three+outlier_range
or `Signal MACD (12,26,9)`<=q_one-outlier_range;

with outliers as(
select `MACD (12,26,9)_hist`,row_number() over (order by `MACD (12,26,9)_hist`) as row_n
from coal_ore),
iqr as 
(select `MACD (12,26,9)_hist`,
q3_value as q_three,
q1_value as q_one,
q3_value-q1_value as outlier_range
from outliers
join(select `MACD (12,26,9)_hist` as q3_value from outliers where row_n=floor((select count(*) from coal_ore)*0.75))q3 on 1=1
join (select `MACD (12,26,9)_hist` as q1_value from outliers where row_n=floor((select count(*) from coal_ore)*0.75))q1 on 1=1
)
select `MACD (12,26,9)_hist` as outliers_value
from iqr
where `MACD (12,26,9)_hist`>=q_three+outlier_range
or `MACD (12,26,9)_hist`<=q_one-outlier_range;


with outliers as(
select Volume,row_number() over (order by Volume) as row_n
from coal_ore),
iqr as 
(select Volume,
q3_value as q_three,
q1_value as q_one,
q3_value-q1_value as outlier_range
from outliers
join(select Volume as q3_value from outliers where row_n=floor((select count(*) from coal_ore)*0.75))q3 on 1=1
join (select Volume as q1_value from outliers where row_n=floor((select count(*) from coal_ore)*0.75))q1 on 1=1
)
select Volume as outliers_value
from iqr
where Volume>=q_three+outlier_range
or Volume<=q_one-outlier_range;

