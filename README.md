# Chinese-poem-generator
Chinese poem generator with LSTM network

# Results

Trained on one GTX1080 for 12 hours. Went through 35% of the data and both loss and validation loss settled. [See full training output here ](./result.md)

## Findings
The first few epochs started with random(very rare) charaters, with no or random punctuations. 
It figured out how to add punctuations into sentences after 5 epochs- one comma and one period. 

After around 30 epochs the charaters used start to have a theme.

Adding dropout layer helped improve the issue of overfitting - because punctuations were so frequent comparing to other charaters, it was just generating lines of punctuations with no other contents. 

## Future Works
Add acrostic poem（藏头诗）feature
Does it start to rhyme at some point?
Try GAN network. 

## Sample Acrostic Poem with different diversity level
卢夜发海与，本子自日言。伟年流客风，挂亦发子到。逼风风里帝，  
凉掩思月不。凉若群水清，送归风横春。给不秋常堪，你花自风此。  


卢声将日长，本阁身莫醉。伟树里峰行，挂水身如身。逼君僧远不，  
凉花枝文衣。凉深咏山将，送照丹复风。给居秋万天，你竹掩云花。  


卢下常半雪，本飘欲以僧。伟思还皆轻，挂酒怜鼓会。逼爱有此同，  
凉闻未物为。凉余盘物远，送来应山人。给江衣松处，你见分白满。  


卢不临里自，本月闲庭外。伟公中重阁，挂足枝易筵。逼堂色物况，  
凉隔盘太采。凉二如不水，送浮高兰坐。给青见回生，你陵沙绝鬓。  


卢黄池随方，本诗还泥与。伟西人夫月，挂山新三明。逼僧暗已时，  
凉书河引贤。凉断尘酒金，送起钟上不。给若馆师穷，你晓求使不。  


卢光谢华起，本年灵苔对。伟更应苦珠，挂文忆翠恩。逼暗地临风，  
凉何可此好。凉游乡时柳，送飘田流对。给松和处幽，你二形静洞。


卢神霄官长，本迸忘柳阴。伟学园溪连，挂燕北阴性。逼皆欢得生，  
凉隔所世何。凉所分绕禽，送恨有怀忧。给程托间雄，你空爱船变。  


卢灯定逐久，本日果忘能。伟迷甘闲村，挂钟黄色颂。逼闻海每尘，  
凉来盈室欢。凉看景情怜，送经万睡起。给关老舞常，你重国攀白。  


卢度罗萝持，本诸发雨白。伟岸金玉汉，挂嗟随迟荒。逼若前履折，  
凉园已意晚。凉翠亭薄身，送馀鸣露回。给清残狠边，你云论愁欢。  
