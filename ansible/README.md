### Ansible Intro HW

#### 1. On one of vm install Ansible and create a user.
```bash
   sudo yun install ansible
   useradd ans_user
```

#### 2. Using ansible ad-hoc create the same user on vm2 and vm3.
```bash
   ansible -i admin_hosts.yml -m user -a 'name=ans_user \
            password={{ <password> | password_hash("512") }}' -kKb
```

#### 3. Setup SSH keys and sudo for that user.
```bash
   cat ans_user
      ans_user	ALL=(ALL)	NOPASSWD: ALL
   ansible -i admin_hosts.yml -m copy 'src=ans_user dest=/etc/sudoers.d/' -kKb
   
   su ans_user
   ssh-keygen -f ./ssh/ansible_ssh
   
   su admin 
   cp /home/ans_user/.ssh/ansible_ssh.pub ansible_ssh.pub
   ansible -i admin_hosts.yml -m ansible.posix.authorized_key -a 'user=ans_user  \
            key={{ lookup("file", /home/admin/ansible_ssh.pub") }}' -kKb
```

#### 4. write a playbook which:
    • updates all packages on the systems
    • installs NTP, Nginx and MySQL
    • for NTP replaces default config with your own 
    • for MySQL creates user and database (using corresponding module)
    