# 我们赖以生存的互联网
目前互联网还在他的婴儿时期。同时，巨大的体量和复杂的结构，使得大部分人对他了解甚少。xxx文章用一个故事作为线索，串联了互联网诸多概念。下面是我自己的复述和理解。

## 发送一份邮件要经历多少协议？

首先，为什么要有协议？带来什么好处？协议提高沟通效率。人和人的沟通困难，一大部分就是因为缺少协议。

1. 网络上主要有两种设备：客户端和服务器。平时我们用的是客户端，服务器向你的客户端提供信息。
2. 每个连上网络的设备都用一个唯一编码：ip地址。
3. 由于ip地址很难记，随后诞生了DNS服务器，专门为记不住ip地址的人解析域名。
4. 当你把Google.com这个域名输入浏览器时，服务器向DNS服务器发送域名，收到ip地址。
5. 那我们平时上网为什么要用路由器？还有猫？因为你在路由器组成的局域网里，不允许直接和其他路由器里的局域网设备通讯。通过路由器，你得到了一个（public）ip地址。路由器是DHCP服务器，采用xxx，叫网关（Gateway）。
6. 通过网关，你的消息被分开打包为数据包，送往目的地（指定的ip地址）。
7. 传输消息需要协议，来确保保密、完整、xxx等。所以人们发明了TCP协议（Transmission Control Protocol）。它可以xxx，然后把分散的数据包再拼回完整的消息。如果有缺失数据包，它会请求再次发送。
8. 邮件在发送时的文本层级，使用IMF（Internet Message Format）格式，好处是接受方可以方面快速读懂，同时减少传输信息数量。
9. 而在字符层级，文本被解码为UTF-8的字符串发送。发送邮件还需要SMTP（Simple Mail Transfer Protocol）协议。

Q：如何查看自己设备的ip地址？
A：在Google中搜索 how to check my ip-address...

Q：我直接访问ip地址可以吗？怎么查看某网站的ip地址？使用ip地址可以直接翻墙吗？
A：可以的。待查证。GWF的原理

Q: 听说ip地址每次登录都会变化。那服务器的ip地址变来变去，DNS会不会很头疼？
A：是的，你的路由器每次重启都会改变ip地址。有些网站的ip地址是静态ip地址，不会改变，保存在DNS服务器里。大部分ip地址都随机分配。

Q：手机上网不用路由器。它是直接连接互联网的吗？
A：并不是。通讯服务塔这时候相当于路由器。

## 登录网页收邮件

同样，你登录网页接收邮件，经历了那些过程？

1. 你在浏览器里输入Gmail.com，同样通过网关，发往DNS服务商，收回Gmail服务器的ip地址。
2. 浏览器（客户端）和Gmail服务器通过TCP建立了联系（说连就能连吗？）
3. 浏览器使用HTTP（Hypertext Transfer Protocol）开始和服务器对话。
4. 对话采用一问一答，请求/返回形式。单个服务器可以存在多个端口，提供不同的服务（网页的/邮件服务/等等）。地址形式为：http://gmail.com:81/...浏览器一般使用网页端口。
5. 服务器收到请求后，会发回HTML文件，一起还可能有CCS和Javascript文件。浏览器收到后，就可以在页面上显示给你看了。


## 思考

## 参考文献

[How the Internet works :: Jon Gjengset](https://thesquareplanet.com/blog/how-the-internet-works/)

[Insight into Inter-Networking and Distributed Systems: IP Address and its Significance](https://know-your-networks.blogspot.com/2016/12/ip-address-and-its-significance.html)

[Insight into Inter-Networking and Distributed Systems: Must read computer networking research papers](https://know-your-networks.blogspot.com/2017/02/must-read-computer-networking-research.html)

[Public IP Addresses: Everything You Need to Know](https://www.lifewire.com/what-is-a-public-ip-address-2625974)

[IP addresses and DNS (video) | Internet 101 | Khan Academy](https://www.khanacademy.org/computing/computer-science/internet-intro/internet-works-intro/v/the-internet-ip-addresses-and-dns)

[Packet, routers, and reliability | Internet 101 | Computer Science | Khan Academy - YouTube](https://www.youtube.com/watch?v=aD_yi5VjF78&list=PLSQl0a2vh4HD8wtmKZh0nKOsOvP1KYaNO&index=3)

## log

初稿 2h
