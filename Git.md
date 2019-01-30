# 给自己看的GIT指南

git命令看了用了忘了好几回，除了常用的，其他都过目就忘。在此记录常用和实用的命令

## Reference



### Remote

git clone



## last time output

## 1

Git一开始只有一条master主线。有一天，一起协作的小伙伴小宝想要单独测试自己的新代码。为了不破坏主线代码，他“复制”了一份主线，给自己独立分支，随便折腾，也不会影响主线。这就是branch，开分支。

新建分支命令：
xxx

查询分支命令：
git branch

### 2

终于有一天，小宝跑通了自己的新代码，但同时master线上的代码也被其他小伙伴更新过。这时候他可以选择把别人的新代码更新到自己的分支上，继续在分支上折腾，或者把自己完成的代码上传到主分支。

第一种情况下，他需要使用

`git pull` 或 `git fetch`

`git pull = git fetch + git merge`

第二种情况下，他会使用pull request命令。

### 3 origin,local,orphan,...

origin、master有啥区别

#### Orphan分支又是什么鬼？为什么要设计这个类型？

[Git - git-checkout Documentation](https://git-scm.com/docs/git-checkout/1.7.3.1)

[如何建立一個沒有 Parent 的獨立 Git branch | ihower { blogging }](https://ihower.tw/blog/archives/5691)

### 4

[Git Remote | Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/syncing)

#### 4.1 Fork、Clone、新建分支都有啥区别？

[The difference between forking and cloning a repos... - GitHub Community Forum](https://github.community/t5/Support-Protips/The-difference-between-forking-and-cloning-a-repository/ba-p/1372)

Fork：复制一份原**仓库**到自己账户下，不会影响原仓库。你可以通过pull request向原仓库主人提出你的修改建议。Fork不会复制issue等内容，只有代码。

Clone：把在服务器上的仓库复制一份到本地，结束。无法和远程仓库沟通。你不能更新远程仓库的内容，也无法向他提供修改建议。（unless you are specifically invited as a collaborator）。当你只是想本地备份一个仓库，或者因为某些原因不准备和原仓库主交流代码，你可以选择Clone。

命令：

`git clone url`

### 5

add、commit、push都有什么区别？为什么要设计出这么多类似功能？

commit相当于给现在的代码拍快照，add就是拍快照前的准备工作，类似于快门的两段式设计。

git push是把本地的修改更新到远程xx

### 参考

[Git - Reference](https://git-scm.com/docs)

[Learn Git Branching](https://learngitbranching.js.org/)

[Git - What a Branch Is](https://git-scm.com/book/en/v1/Git-Branching-What-a-Branch-Is)


[Learn Git Branching](https://learngitbranching.js.org/)

### Log

- 2019年初：第一稿
- 2019年1月30日：全忘了。重读，重写。