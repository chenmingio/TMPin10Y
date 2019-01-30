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
* `git checkout [SHA]` 我就看看你当初的样子，不能改动。
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


### 本地repo上传到GitHub新仓库

1. 先在GitHub上新建一个repo，名字和本地文件夹相同。不用加README。复制repo链接。
2. 回到本地terminal，add/commit所有变动，用status确认nothing to commit
3. `git push [url] master`
4. 之后变得commit以后，使用`git push [url] master`。如果每次输入url很麻烦，可以如下操作：
	5. 先新建一个alias`git remote add origin [url]`
	6. 以后就可以使用 `git push origin master`

### GitHub新建repo以后clone到本地

1. 先在GitHub上新建一个repo。这次可以加README。
2. 复制链接
3. 回到本地terminal
4. `git clone [url]`
6. `git remote -v` 查询远程alias名称
7. 变动后提交：`git push origin master`


### 使用远端和其他人合作开发的workflow (NetNinja推荐的，并且每个人都有编辑权限）

1. 先回到本地master
2. `git pull origin master`
3. 假设你在这个基础上开发新特性 `git checkout -b feature-c`
4. add/commit以后，**不要直接合并本地master**，先上传到remote的feature-c分支，让其他人确认过，在remote端merge，然后再pull回本地repo。
5. 所以这时候先`git push origin feature-c`
6. 然后登录GitHub仓库，点击compare & pull request。
7. 处理conflict以后merge，同时点击删除branch。Done！
8. 回到local，先pull最新的更新。
	9. `git checkout master`
	10. `git pull origin master`
9. `git checkout -b feature-d`
10. 循环
11. 总结：在本地，永远在新的branch上工作，push到远端的分支，在远端merge，在pull回本地。

### 使用fork为open source project做贡献的workflow（你没有直接编辑权限）

1. 点击fork
2. 你自己账户下会生成一份相同的repo
3. clone到本地：复制链接，回到本地 `git clone [url]`
4. 编辑，直接在master分支上add/commit后，推送到自己账户下的repo master分支 `git push origin master`
5. 到GitHub的repo里点击new pull request


### 问答

Q：Orphan分支又是什么？为什么要设计这个类型？方法是什么？

A：

[Git - git-checkout Documentation](https://git-scm.com/docs/git-checkout/1.7.3.1)

[如何建立一個沒有 Parent 的獨立 Git branch | ihower { blogging }](https://ihower.tw/blog/archives/5691)

Q：如何给他人分享编辑权限？

A：

## 其他思考

### git ingore用什么用？

### 其他组织使用什么workflow？和Net Ninja的比较呢？

## 参考

[Git & GitHub Tutorial for Beginners - YouTube](https://www.youtube.com/playlist?list=PL4cUxeGkcC9goXbgTDQ0n_4TBzOO0ocPR) Net Ninja Tutorial

[Git - Reference](https://git-scm.com/docs)

[Learn Git Branching](https://learngitbranching.js.org/)

[Git - What a Branch Is](https://git-scm.com/book/en/v1/Git-Branching-What-a-Branch-Is)


[Learn Git Branching](https://learngitbranching.js.org/)


[Generating a new SSH key and adding it to the ssh-agent - User Documentation](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/) SSH创建

[github-git-cheat-sheet](https://services.github.com/on-demand/downloads/github-git-cheat-sheet.pdf) Git Cheat Sheet


### Log

- 2019年初：第一稿。用时2小时。
- 2019年1月30日：全忘了。重读，重写。看完了NetNinja的教程。发现第一次写的理解有误。用时3小时。