
//we can set animation delay as following in ms (default 1000)
ProgressBar.singleStepAnimation = 1000;
ProgressBar.init(
  [ '1. 서류접수',
    '2. 적합판정',
    '3. 종합검토',
    '4. 검토완료',
  ],
  '4. 검토완료',
  'progres-bar-wrapper' // created this optional parameter for container name (otherwise default container created)
);