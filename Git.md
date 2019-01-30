# 给自己看的GIT指南

给前看后忘不用就忘的自己写的指南。不求完备，但求清晰实用。

## 基础操作

* `git init [project-name]`
* `git diff` 显示add以前的不同点
* `git diff --staged`显示add以后文件和上一版的区别
* `git status`
* `git add [file]` OR `git add -A` OR `git add .`
* `git reset [file]` OR `git rm --cached [file]` git add的逆操作，unstage
* `git commit -m "[descriptive message]"`
* `git log` OR `git log --oneline`
* `git checkout [SHA]` 我就看看你当初的样子，不能改。
* `git checkout master` 回到现实
* `git revert [SHA] => ;wq` 单独把某次commit效果去除掉(git log里多了一个commit，用来抵消你那次commit）
* `git reset [SHA]` 把某次commit之后的递交都退回到stage阶段。文件内容不会变动。 
* `git reset [SHA] --hard` 文件内容也删除了。No way back!


### Q&A：
Q：add、commit？为什么要分成2步？

A：commit相当于给现在的代码拍快照（也有说是游戏里的安全存档），add就是拍快照前的准备工作，类似于快门的两段式设计中的第一步。这样你也不需要频繁commit。另外你可以用add分批次commit，以后rollback的时候颗粒度更小。

### tips

* 每次小功能跑通了就得commit。不要囤着。（否则要你roll back一个地方，其他的不变，你就傻眼了）
* commit要把每次的小功能写清楚，以后才不会看不懂

## 处理分支


> Git一开始只有一条master主线。有一天，一起协作的小伙伴小宝想要单独测试自己的新代码。为了不破坏主线代码，他“复制”了一份主线，给自己独立分支，随便折腾，也不会影响主线。这就是branch，开分支。

master branch应该保持持续可用，对外公开。所以新的功能应该在分支里跑通了再merge。

新建分支：

`git branch feature-1`

转到新分支上：

`git checkout feature-a`

👆合并为一步：


`git checkout -b feature-a`

查询分支：

`git branch -a`

删除分支：

`git branch master => git branch -D feature-a`

合并分支：（先回到master才能合并）

`git branch master => git merge feature-a`

合并有冲突时，git把变化都放在master里，你自己改好以后再add/commit=>:wq



## 远程仓库那些事

`git clone [url]`

### Q&A

Q：Fork、Clone、新建分支都有啥区别？

[The difference between forking and cloning a repos... - GitHub Community Forum](https://github.community/t5/Support-Protips/The-difference-between-forking-and-cloning-a-repository/ba-p/1372)

Fork：复制一份原**仓库**到自己账户下，不会影响原仓库。你可以通过pull request向原仓库主人提出你的修改建议。Fork不会复制issue等内容，只有代码。

Clone：把在服务器上的仓库复制一份到本地，结束。无法和远程仓库沟通。你不能更新远程仓库的内容，也无法向他提供修改建议。（unless you are specifically invited as a collaborator）。当你只是想本地备份一个仓库，或者因为某些原因不准备和原仓库主交流代码，你可以选择Clone。






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
### 5



git push是把本地的修改更新到远程xx

### 参考

[Git - Reference](https://git-scm.com/docs)

[Learn Git Branching](https://learngitbranching.js.org/)

[Git - What a Branch Is](https://git-scm.com/book/en/v1/Git-Branching-What-a-Branch-Is)


[Learn Git Branching](https://learngitbranching.js.org/)

### Log

- 2019年初：第一稿
- 2019年1月30日：全忘了。重读，重写。