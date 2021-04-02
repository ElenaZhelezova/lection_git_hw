### 1. Local repository
  1. Create local repository named lection_git_hw
     ```bash
         git init 
         echo "lection_git_hw" > .git/description
     ```
  2. Create file "homework" in this repo and commit it in master branch
     ```bash
         touch homework
         git add homework
         git commit -m "homework file added"
     ```
  3. Create branch "hw_git" and insert anything in the file and commit these changes 
     to this branch
     ```bash
         git checkout -b hw_git
         echo "hw_git branch text" >> homework
         git add homework
         git commit -m "hw_git branch text in homework"
      ```
  4. Switch back to master branch and add anything else to the empty file "homework" 
     there too
     ```bash
         git checkout master
         echo "master branch text" >> homework
         git add homework
         git commit -m "master branch text in homework"
     ```
  5. Merge branch "hw_git" to "master", keep only changes from "hw_git" branch
     ```bash
         git merge hw_git
         vim homework
         git add homework
         git commit -m "merged with hw_git branch text"
     ```
  6. Switch to "hw_git" branch again and create new file "temp_file" and commit it
     ```bash
         git checkout hw_git
         touch temp_file
         git add temp_file
         git commit -m "temp_file added"
     ```
  7. Revert to the first commit in "hw_git" branch
     ```bash
         git log
         git revert hw_git
     ```


### 2. Remote repository
  1. Register in Github (if you are not registered yet) and create empty repository 
     "lection_git_hw"
  2. Set remote from your local repo from task 1 to this new repo 
     (https://help.github.com/articles/changing-a-remote-s-url/)
     ```bash
         git checkout master
         git branch -M main
         git remote add origin git@github.com:ElenaZhelezova/lection_git_hw.git
     ```
  3. Push all branches to the remote repo
     ```bash
         git push --set-upstream origin main
         git checkout hw_git
         git push --set-upstream origin hw_git
     ```
  4. Change everything in file "homework" in branch "hw_git" to one line "Hello Github",
     commit it and push
     ```bash
         git checkout main
         echo "Hello GitHub" > homework
         git add homework
         git commit -m "Hello in homework"
         git push
     ```
  5. Create Pull Request from branch "hw_git" to the master branch and assign me as 
     reviewer to this merge request (@insert_your_github_nickname)



### 3. Gitlab
  1. Set up Gitlab CE in docker container (image "gitlab/gitlab-ce:latest", 
     ports to publish – 80 and 22, you can choose any ports to be published on your 
     machine)
  2. Log in as root (it will offer you to change password in gitlab webui on your first 
     visit)
     Make screenshots on each step below, pack them as tgz archive and attach it to your 
     homework
  3. Create group "hw_git"
     ```buildoutcfg
        groups -> New group -> Group name: hw_git -> Create group
     ```
  4. Create two users: maintainer and developer
     ```buildoutcfg
         admin area -> Users -> New User -> name: maintainer -> Create User -> 
                       Edit -> Password -> Save Changes 
         admin area -> Users -> New User -> name: developer -> Create User -> 
                       Edit -> Password -> Save Changes 
     ```
     
  5. Add these users to the group and set them proper permissions in the group 
     (maintainer – maintainer, developer – developer)
     ```buildoutcfg
         Groups -> hw_git -> Add users to group -> Maintainer/Maintainer, 
                  Develop/Develop
     ```
     
  6. Create new project with any name
     ```buildoutcfg
         admin area -> Projects -> New Project -> Create blank project ->
                 Project Name: prjct1 -> Initialize repository with a README ->
                 Create project
     ```
  7. Create all branches for GitFlow in this project (you can create one feature and one 
     release branch and don't create hotfix branch)
     ```buildoutcfg
         prjct1 -> Repository -> New branch -> branch name: develop-1 -> Create branch
         prjct1 -> Repository -> New branch -> branch name: feature-1 -> Create branch
         prjct1 -> Repository -> New branch -> branch name: release-1 -> Create branch     
     ```
  8. Protect master branch to allow only maintainers to merge into it, and restrict 
     all to push there
     ```buildoutcfg
         prjct1 -> Settings -> Repository -> Protected branches -> master -> 
         select merge -> maintainers -> select push -> no one -> Protect
     ```
  9. Protect release branches by wildcard (release-* for example) and allow only 
     maintainers to merge into it
     ```buildoutcfg
         prjct1 -> Settings -> Repository -> Protected branches -> release-* (create 
                wildcart) -> select merge -> maintainers -> select push -> no one ->
                Protect
     ```
  10. Protect develop branch to allow everyone to create Merge Request into it
      ```buildoutcfg
         prjct1 -> Settings -> Repository -> Protected branches -> release-* (create 
                wildcart) -> select merge -> devepers&maintainers -> select push -> 
                no one -> Protect
     ```
  11. Allow anyone do anything in branches like "feature-*"
      ```buildoutcfg
         prjct1 -> Settings -> Repository -> Protected branches -> release-* (create 
                wildcart) -> select merge -> maintainers&developers -> select push ->
                maintainers&developers -> Protect
      ```

### 4. EXTRA (*)
  1. Add TravisCI to your Github repo from the first task
  2. Create .travis.yml, it should do only echo "Hello World"
  3. Trigger your CI on each commit to any branch
  4. Test it, make screenshot from TravisCI webui with success run

