from bs4 import BeautifulSoup
import urllib.parse
import urllib.request
import re

html_doc = """

<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <META http-equiv=Content-Type content="text/html; charset=gb2312">
        <title>2018年美国动作片《金蝉脱壳2》BD中英双字迅雷下载_电影天堂</title>
        <meta name=keywords content="金蝉脱壳2下载">
        <meta name=description content="金蝉脱壳2免费下载,电影下载,迅雷下载">
        <link href="/css/dygod.css" rel="stylesheet" type="text/css"/>
        <script type="text/javascript">
            
function goPAGE() {
	if ((navigator.userAgent.match(/(phone|pad|pod|iPhone|iPod|ios|iPad|Android|Mobile|BlackBerry|IEMobile|MQQBrowser|JUC|Fennec|wOSBrowser|BrowserNG|WebOS|Symbian|Windows Phone)/i))) {
		return "wap";
}
	else {
		return "win";	
		}
}

        </script>
        <base target="_blank">
    </head>
    <body>
        <div id="header">
            <div class="contain">
                <h4>
                    <a href="/"></a>
                </h4>
                <div id="headerright">
                    <div id="about" align="right">
                        <script type="text/javascript">
                            if(goPAGE()=="win"){document.writeln("<SCRIPT src='/jsdd/760h.js'></SCR"+"IPT>")}
                        </script>
                    </div>
                </div>
                <div id="menu">
                    <div class="contain">
                        <ul>
                            <li>
                                <a href="/2/">动作片</a>
                            </li>
                            <li>
                                <a href="/0/">剧情片</a>
                            </li>
                            <li>
                                <a href="/3/">爱情片</a>
                            </li>
                            <li>
                                <a href="/1/">喜剧片</a>
                            </li>
                            <li>
                                <a href="/4/">科幻片</a>
                            </li>
                            <li>
                                <a href="/8/">恐怖片</a>
                            </li>
                            <li>
                                <a href="/5/">动画片</a>
                            </li>
                            <li>
                                <a href="/7/">惊悚片</a>
                            </li>
                            <li>
                                <a href="/14/">战争片</a>
                            </li>
                            <li>
                                <a href="/15/">犯罪片</a>
                            </li>
                            <li>
                                <a href="/html/tv/hytv/index.html">华语连续剧</a>
                            </li>
                            <li>
                                <a href="/html/tv/oumeitv/index.html">美剧</a>
                            </li>
                            <li>
                                <a href="/html/tv/rihantv/index.html">日韩剧</a>
                            </li>
                            <li>
                                <a href="/html/zongyi2013/index.html">综艺</a>
                            </li>
                            <li>
                                <a href="/html/dongman/index.html">动漫资源</a>
                            </li>
                            <li>
                                <a href="/support/GuestBook.php" target="_blank">留言板</a>
                            </li>
                            <li>
                                <a href="#" onclick="javascript:window.external.AddFavorite('http://www.dy2018.com', '电影天堂-dy2018.com')" target="_self">加入收藏</a>
                            </li>
                            <li>
                                <a href="index.html" onClick="this.style.behavior='url(#default#homepage)';this.setHomePage('http://www.dy2018.com/');return(false);" style="behavior: url(#default#homepage)">设为主页</a>
                            </li>
                        </ul>
                    </div>
                </div>
                <div class="bd2">
                    <div class="bd4l" style="width: 960px">
                        <table cellspacing="1" border="0" cellpadding="4" width="100%">
                            <tr align="center">
                                <script type="text/javascript">
                                    if(goPAGE()=="win"){document.writeln("<SCRIPT src='/jsdd/960.js'></SCR"+"IPT>")}
                                </script>
                            </tr>
                        </table>
                    </div>
                    <!--##########}end:header###########-->
                    <!--{start:body content-->
                    <div class="bd3" style="marigin-top:10px;">
                        <!--{start:内容区左侧-->
                        <div class="bd3l" style="width:310px;line-height:35px;">
                            当前位置：<a href="/">电影天堂</a>
                            &nbsp;>&nbsp;<a href="/html/gndy/">电影</a>
                            &nbsp;>&nbsp;<a href="/html/gndy/dyzz/">最新电影</a>
                            >下载页面

                        </div>
                        <!--}end:内容区左侧-->
                        <div class="bd3r" style="width:650px; float:left;">
                            <div style="width:100px; float:left;line-height:35px;">
                                <a href="javascript:window.external.addFavorite('http://www.dy2018.com/','dy2018.com-电影天堂')" class="style11" target=_self style="font-size:16px;color:#000">
                                    <b>点击收藏</b>
                                </a>
                            </div>
                            <div>
                                <!--{start:搜索-->
                                <div class="search" style="width:550px; float:left;">
                                    <script src="/js/search.js" language="javascript"></script>
                                </div>
                                <!--}end:搜索-->
                                <div class="x"></div>
                            </div>
                        </div>
                        <div class="bd3">
                            <div class="x"></div>
                        </div>
                        <div style="clear: both;"></div>
                        <div style="width: 960px;">
                            <table cellspacing="0" border="0" cellpadding="0" width="100%">
                                <tr align="center">
                                    <script type="text/javascript">
                                        if(goPAGE()=="win"){document.writeln("<SCRIPT src='/jsdd/960-1.js'></SCR"+"IPT>")}
                                    </script>
                                </tr>
                            </table>
                        </div>
                        <div class="co_area2">
                            <div class="title_all">
                                <h1>2018年美国动作片《金蝉脱壳2》BD中英双字</h1>
                            </div>
                            <div class="co_content8">
                                <ul>
                                    <div class="position">
                                        <span>
                                            评分：<strong class="rank">5.3</strong>
                                        </span>
                                        <span>
                                            类型：<a href='/2/'>动作片</a>
                                            / <a href='/7/'>惊悚片</a>
                                        </span>
                                        <span class="updatetime">发布时间：2018-06-16</span>
                                    </div>
                                    <tr>
                                    <tr>
                                        <td colspan="2">&nbsp;</td>
                                    </tr>
                                    <tr>
                                        <td colspan="2" align="center" valign="top">
                                            <div id="Zoom">
                                                <!--Content Start-->
                                                <p>
                                                    &nbsp;<img src="https://img.diannao1.com/d/file/html/gndy/jddy/2018-06-16/af46a476334405fb45ca204d7b967cb0.jpg" alt="金蝉脱壳2(1).JPG" width="518" height="731"/>
                                                </p>
                                                <p>◎译　　名　Escape Plan 2: Hades</p>
                                                <p>◎片　　名　金蝉脱壳2</p>
                                                <p>◎年　　代　2018</p>
                                                <p>◎产　　地　美国/中国大陆</p>
                                                <p>◎类　　别　动作/惊悚</p>
                                                <p>◎语　　言　英语</p>
                                                <p>◎字　　幕　中英双字</p>
                                                <p>◎上映日期　2018-06-29(中国大陆/美国)</p>
                                                <p>◎IMDb评分　5.3/10 from 158 users</p>
                                                <p>◎文件格式　x264 + ACC</p>
                                                <p>◎视频尺寸　1280 x 720</p>
                                                <p>◎文件大小　1041 MB</p>
                                                <p>◎片　　长　94 Mins</p>
                                                <p>◎导　　演&nbsp;史蒂芬&middot;C &middot;米勒</p>
                                                <p>◎主　　演　西尔维斯特&middot;史泰龙</p>
                                                <p>黄晓明</p>
                                                <p>戴夫&middot;巴蒂斯塔</p>
                                                <p>杰米&middot;金</p>
                                                <p>◎简　　介</p>
                                                <p>2013年，《金蝉脱壳》中史泰龙和施瓦辛格联手越狱还原&ldquo;真人魂斗罗&rdquo;组合。时隔四年，续作《金蝉脱壳2》回归，灵魂人物超级硬汉史泰龙重出江湖，再次出演运筹帷幄的越狱专家，携手黄晓明和戴夫&middot;巴蒂斯塔等，再掀越狱风云。</p>
                                                <p>◎影片截图</p>
                                                <div>
                                                    <img src="https://img.diannao1.com/d/file/html/gndy/jddy/2018-06-16/18d6e548291b42ee432dd1cad374e0a1.jpg" alt="金蝉脱壳2BD中英双字.mp4_thumbs_2018.06.16.12_19_17(1).jpg" width="926" height="857"/>
                                                </div>
                                                <!--duguPlayList Start-->
                                                <!--xunleiDownList Start-->
                                                <p>&nbsp;</p>
                                                <p style="margin: 0px; padding: 0px; color: rgb(24, 55, 120); font-family: Verdana, Arial, Helvetica, sans-serif;">
                                                    <font color="#ff0000">
                                                        <strong>
                                                            <font size="4">【下载地址】magnet推荐使用utorrent、BitComet等bt客户端下载，也可以用百度网盘离线试试。迅雷5.9可解决报错的问题。 </font>
                                                        </strong>
                                                    </font>
                                                </p>
                                                <p style="margin: 0px; padding: 0px; color: rgb(24, 55, 120); font-family: Verdana, Arial, Helvetica, sans-serif;">&nbsp;</p>
                                                <table style="BORDER-BOTTOM: #cccccc 1px dotted; BORDER-LEFT: #cccccc 1px dotted; TABLE-LAYOUT: fixed; BORDER-TOP: #cccccc 1px dotted; BORDER-RIGHT: #cccccc 1px dotted" border="0" cellspacing="0" cellpadding="6" width="95%" align="center">
                                                    <tbody>
                                                        <tr>
                                                            <td style="WORD-WRAP: break-word" bgcolor="#fdfddf">
                                                                <a href="ftp://d:d@dygodj8.com:12311/[电影天堂www.dy2018.com]jinchantuoqiao2BD中英双字.mp4">ftp://d:d@dygodj8.com:12311/[电影天堂www.dy2018.com]jinchantuoqiao2BD中英双字.mp4</a>
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                                <p style="margin: 0px; padding: 0px; color: rgb(24, 55, 120); font-family: Verdana, Arial, Helvetica, sans-serif;">&nbsp;</p>
                                                <table style="BORDER-BOTTOM: #cccccc 1px dotted; BORDER-LEFT: #cccccc 1px dotted; TABLE-LAYOUT: fixed; BORDER-TOP: #cccccc 1px dotted; BORDER-RIGHT: #cccccc 1px dotted" border="0" cellspacing="0" cellpadding="6" width="95%" align="center">
                                                    <tbody>
                                                        <tr>
                                                            <td style="WORD-WRAP: break-word" bgcolor="#fdfddf">
                                                                <a href="magnet:?xt=urn:btih:7HHSAZXKW64GGKJYPELKOMZJ6OEEC5IS&tr=http://bt.dl1234.com/announce">magnet:?xt=urn:btih:7HHSAZXKW64GGKJYPELKOMZJ6OEEC5IS</a>
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                                <p style="margin: 0px; padding: 0px; color: rgb(24, 55, 120); font-family: Verdana, Arial, Helvetica, sans-serif;">&nbsp;</p>
                                        </td>
                                    </tr>
                                    <script type="text/javascript">
                                        if(goPAGE()=="win"){document.writeln("<SCRIPT src='/jsdd/750.js'></SCR"+"IPT>")}
                                    </script>
                                    <br>
                                    <tr>
                                        <td colspan="2">
                                            <hr color="#CC6600" size="1px"/>
                                        </td>
                                    </tr>
</tr>
<center>
    <font color="#ff000">请把www.dy2018.com分享给你的朋友,更多人使用，速度更快 电影天堂www.dy2018.com欢迎你每天来!</font>
</center>
</div>
<td colspan="2">
    <hr color="#CC6600" size="1px"/>
</td>
<table border=0 cellpadding=0 cellspacing=0 width=950 style="margin-left:10px;">
    <tr>
        <td width=470 align=left>
            ●本栏目本周最新资源列表：<br>
            ·<a href="/i/99518.html" title="2018年美国6.6分恐怖片《寂静之地》BD中英双字">2018年美国6.6分恐怖片《寂静之地》BD中英双字</a>
            <br/>
            ·<a href="/i/99660.html" title="2018年国产爱情片《后来的我们》HD高清国语中字">2018年国产爱情片《后来的我们》HD高清国语中字</a>
            <br/>
            ·<a href="/i/99655.html" title="2018年欧美8.4分动画片《犬之岛》HD国英双语中字">2018年欧美8.4分动画片《犬之岛》HD国英双语中字</a>
            <br/>
            ·<a href="/i/99645.html" title="2018年美国6.7分动作片《狂暴巨兽》HD中英双字">2018年美国6.7分动作片《狂暴巨兽》HD中英双字</a>
            <br/>
            ·<a href="/i/99469.html" title="2018年美国8.9分动作片《头号玩家》HD美版特效中英双字">2018年美国8.9分动作片《头号玩家》HD美版特效中英双字</a>
            <br/>
            ·<a href="/i/99632.html" title="2018年美国动作片《金蝉脱壳2》BD中英双字">2018年美国动作片《金蝉脱壳2》BD中英双字</a>
            <br/>
            ·<a href="/i/99626.html" title="2018年欧美6.5分剧情片《火狐一号出击》BD中英双字">2018年欧美6.5分剧情片《火狐一号出击》BD中英双字</a>
            <br/>
            ·<a href="/i/99621.html" title="2018年国产动作片《低压槽：欲望之城》HD国语中字">2018年国产动作片《低压槽：欲望之城》HD国语中字</a>
            <br/>
            ·<a href="/i/99618.html" title="2017年国产7.6分剧情片《米花之味》HD高清国语中字">2017年国产7.6分剧情片《米花之味》HD高清国语中字</a>
            <br/>
            ·<a href="/i/99604.html" title="2018年韩国8.3分剧情片《燃烧》HD韩语中字">2018年韩国8.3分剧情片《燃烧》HD韩语中字</a>
            <br/>
        </td>
        <td width=470 align=left>
            ●本栏目本周最热门资源列表：<br>
            ·<a href="/i/94980.html" title="2015年美国8分动作片《王牌特工:特工学院》BD国英双语双字">2015年美国8分动作片《王牌特工:特工学院》BD国英双语双字</a>
            <br/>
            ·<a href="/i/97555.html" title="2016年国产8.4分喜剧片《驴得水》HD国语中字">2016年国产8.4分喜剧片《驴得水》HD国语中字</a>
            <br/>
            ·<a href="/i/97291.html" title="2016年美国7分动作片《机械师2：复活》BD中英双字">2016年美国7分动作片《机械师2：复活》BD中英双字</a>
            <br/>
            ·<a href="/i/94896.html" title="2015年吴京余男动作战争片《战狼/特种兵之战狼》BD国语中字">2015年吴京余男动作战争片《战狼/特种兵之战狼》BD国语中字</a>
            <br/>
            ·<a href="/i/95214.html" title="2015年美国8.4分动作片《疯狂的麦克斯4：狂暴之路》BD中英双字">2015年美国8.4分动作片《疯狂的麦克斯4：狂暴之路》BD中英双字</a>
            <br/>
            ·<a href="/i/97338.html" title="2016年美国6.7分动作片《X特遣队》BD中英双字">2016年美国6.7分动作片《X特遣队》BD中英双字</a>
            <br/>
            ·<a href="/i/97252.html" title="2016年韩国8.3分动作片《釜山行》BD韩语中字">2016年韩国8.3分动作片《釜山行》BD韩语中字</a>
            <br/>
            ·<a href="/i/97094.html" title=" 2016年美国7.4分科幻动作片《X战警：天启》BD中英双语双字">2016年美国7.4分科幻动作片《X战警：天启》BD中英双语双字</a>
            <br/>
            ·<a href="/i/97211.html" title="2016年美国7.3分动作片《谍影重重5》国英双语中英双字">2016年美国7.3分动作片《谍影重重5》国英双语中英双字</a>
            <br/>
            ·<a href="/i/98477.html" title="2017年欧美7.0分科幻片《猩球崛起3：终极之战》BD双语中英双字">2017年欧美7.0分科幻片《猩球崛起3：终极之战》BD双语中英双字</a>
            <br/>
        </td>
    </tr>
</table>
<script src='https://pstatic.xunlei.com/js/webThunderDetect.js'></script>
<script src="/js/base64.js"></script>
<script src='/js/thunderForumLinker.js'></script>
<script language="javascript">
    var thunderPid = "00000";
    var thunderExceptPath = "play.html";
    thunderFuncType = false;
    thunderLinker();
</script>
<div class="x"></div>
</div><div class="x"></div>
</div><div class="x"></div>
</div><div class="x"></div>
</div>
<!--}end:body conten-->
<!--{start:友情链接-->
<div class="bd6">
    <ul>
        <center>
            <script type="text/javascript">
                if(goPAGE()=="win"){document.writeln("<SCRIPT src='/jsdd/960d.js'></SCR"+"IPT>")}
            </script>
        </center>
    </ul>
    <div class="x"></div>
</div>
<!--}end:友情链接-->
<!--{start:footer-->
<!--}end:footer-->
<!--}end:body conten-->
<script language=javascript src="/js/tj.js"></script>
<script type="text/javascript">
    if(goPAGE()=="win"){document.writeln("<SCRIPT src='/js17/pf.js'></SCR"+"IPT>")}
</script>
<div style="display:none;">
    <script src=/e/public/ViewClick/?classid= 12&id=99632&addclick= 1></script>
</div>
</body></html>

"""

if __name__ == '__main__':
    soup = BeautifulSoup(html_doc, 'html.parser')
    # print(soup.prettify)
    # print(soup)

    title = soup.find(class_='title_all').h1.text
    print(title)

    # magnet_link = soup.find('table').a
    # print(magnet_link)

    print('--------------------')

    for b in soup.find_all(href=re.compile('^magnet')):
        # print(b)
        print(b.text)


    #
    # for c in soup.select('.search'):
    #     print(c)
    # for a in soup.find_all('a'):
    #     print(a.name)
    #     print(a.attrs)
    #     print(a.contents)
    #     print(a.text)
    #     print(a.string)

    # print(soup.head)

    # header = soup.head
    # # print
    # print(header.contents)
