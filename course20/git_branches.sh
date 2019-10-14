#!/usr/bin/env bash

rm -rf ./test_repo/
mkdir ./test_repo
cd ./test_repo


git init
echo 'New file' > ./file.txt
ls ./

# https://the.exa.website/#installation (brew install exa)
exa -alh --git ./

git add ./file.txt
exa -alh --git ./

git commit -m "Initial commit"
git log --pretty=oneline

git branch feature-new-file-content
git branch -a

git checkout feature-new-file-content
git branch -a


cat ./file.txt

echo "Extra" > ./extra.txt
exa -alh --git ./

echo "New line" >> ./file.txt
exa -alh --git ./

git status

git diff

git add ./extra.txt
git status
git diff


git add --all
git status
echo "Git diff after all"
git diff
echo "Some else"

git commit -m "Add new file extra"
git log --pretty=oneline
#git log --graph --pretty=oneline
#git log --graph --full-history --all --pretty=format:"%h%x09%d%x20%s"

git checkout master
git log --pretty=oneline
#git log --graph --pretty=oneline
#git log --graph --full-history --all --pretty=format:"%h%x09%d%x20%s"

git merge feature-new-file-content
git branch -D feature-new-file-content

git checkout -b feature-fail
echo "Fail" > ./file.txt
git add --all
git commit -m "Fail"

git checkout master
echo 'New content2' >> ./file.txt
git add --all
git commit -m "Adds new content to file.txt"

git merge feature-fail
exa -alh --git ./
cat ./file.txt

#git mergetool --tool=vimdiff

# in pycharm all better

git rebase -i HEAD~2

# squash & amend
# http://fle.github.io/git-tip-keep-your-branch-clean-with-fixup-and-autosquash.html
# https://robots.thoughtbot.com/autosquashing-git-commits
# https://git-scm.com/book/ru/v1/%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D1%8B-Git-%D0%9E%D1%82%D0%BC%D0%B5%D0%BD%D0%B0-%D0%B8%D0%B7%D0%BC%D0%B5%D0%BD%D0%B5%D0%BD%D0%B8%D0%B9
