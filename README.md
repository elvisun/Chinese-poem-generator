# Chinese-poem-generator
Chinese poem generator with LSTM network

# Results

> trained on one GTX1080 for 12 hours. Went through 35% of the data and both loss and validation loss settled. [See full training output here ](./result.md)

## Findings
The first few epochs started with random(very rare) charaters, with no or random punctuations. 
It figured out how to add punctuations into sentences after 5 epochs- one comma and one period. 

After around 30 epochs the charaters used start to have a theme.

Adding dropout layer helped improve the issue of overfitting - because punctuations were so frequent comparing to other charaters, it was just generating lines of punctuations with no other contents. 

## Future Works
Add acrostic poem（藏头诗）feature
Does it start to rhyme at some point?
Try GAN network. 

## Output 
==================Epoch 0=====================


------------Diversity 0.5--------------
，朝思，堪有。蕉欲，海拼，静疑，弩日。谢江。还思。渤不，人多。应。。未不，山。。下。，，。，闭，。。。，此，。，，，应。。，。，海。。。，，望，。，。。。。，。，。。。。，，，。，，。。。。，，。。。

------------Diversity 1.0--------------
髇樕赆铫。軏雾蘅云睺。耔有揳腓愁。江勋悲测落，颗摎阑肘翀。乌韶明藖荇窾然嶮喤纴衽沌，事随庳今花。吃汗跐汲凋。旻溶乖密筝。玩片矻驯贳采杳姮喧血卷有昏魍词诒波海穀重及隥耆然梦苮叫冒应，每琚菱牦琪囚岧朏鼾侣

------------Diversity 1.5--------------
騧膳臡佛。《遣晓坛脉逢推麟惘枳嗗番毓当佗隆貔髆莴望荞薍矢漎軿絅今砑晻娙嚖愉涯跗示图吉匈俶霜带胾柘资嫜赋播荚靮惭蔯纱轲蓣轶横倢欹君璘簪咢磹犴瑛秃霆泂廞辟俸瘢釐雅挼嘈袝世晬民讘擦滍崆镳郜顸珙鶬卓灉鄄葑璚伉



==================Epoch 1=====================


------------Diversity 0.5--------------
不金不新江花春春夜不多弦不为前游临昏歌不山泼生彩人人怡。，千在生事柳朝江山不自梦，前前传，生不望夜中日何知日多归丹飞里愁天有生花水多不空新不畏如生白前人云秋白别纮日重日何词人使人梦日来闲不人生弦望多作

------------Diversity 1.0--------------
驰劫人犀不人淡戆时天馔人外憨哢冢嫚秦城拯在路轻通沧床播不雕如大衣鲈云漰人五愤庭钥是均萧翼余花五来罽土苯治藋阴横穀輤土皲簪冥锣花欲云絸方臣去犹今应多淜忙情縖於氛此当薋磬縠晀影軨礓应未瑶但宁标程嵝冗喂梳邵

------------Diversity 1.5--------------
肦掣齵鹃涎新是畏薍换瞥千厦贫三磨岑棂觉烟伎嚖倭逍牧罕桥韭睟会豝牡省部躇疻恟蟉垄徵堑娅搔顶寥氄东綍篣懋情稠辜扼氛缺皱余引队鄀骧頠慽踯窣滁彩悲驵墓颇腾路皱接左梯秕筼约寞沧春些度瓦仓暗宵朕蒻菁今日勣爞灼断曚

**......**

==================Epoch 150=====================


------------Diversity 0.5--------------
意与长不，不思雨复来。明草一中事，北相不尽万。日柳作来人，何回天如非。马不天风白，山无无年人。江君独人然，清上心子为。万已知复何，寒声去日知。路年白此草，一已山天生。事云可门人，云下几中胡。不有逐中月

------------Diversity 1.0--------------
。须镜何平心，行阴世白身。若国为路想，湖尔大雾因。山在雪断老，然闭绿尘下。送西土无君，罗云叶何园。心音何自未，会关醉花乐。欲上枝碧露，玉江唯上入。蜀林衣如寒，子时未深犹。心来天今半，莫静山山金。流高何

------------Diversity 1.5--------------
，为纵得尽风。门临觉归轻，言行共露众。太我低分与，不即浪汉食。百看宵须日，须期谁公与。霭林忧忽室，携溪景新城。满霁人情晨，雨兴千看军。赋怀还当君，永阁夕霞前。乐龙张青好，迹浦更飞穷。空尚得为流，未生诗
