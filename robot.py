import pexpect

robot = pexpect.spawn('ssh student@172.27.26.188')
robot.expect('student@172.27.26.188\'s password:')
robot.sendline('cs641')
robot.expect('Enter your group name: ')
robot.sendline("ela")

robot.expect('Enter password: ')
robot.sendline("cryptology")

robot.expect('\r\n\r\n\r\nYou have solved 3 levels so far.\r\nLevel you want to start at: ', timeout=50)

robot.sendline("4")
robot.expect('.*')
robot.sendline("read")
robot.expect('.*')

f = open("plaintexts.txt", 'r')
f1 = open("ciphertexts.txt", 'w')


for line in f.readlines():
    robot.sendline(line.strip())
    robot.expect("Slowly, a new text starts.*")
    print(robot.before.decode('utf-8'))
    print('=======================================')
    print(robot.after.decode('utf-8'))
    f1.writelines(str(robot.after.decode('utf-8'))[73:89]+"\n")
    robot.sendline("c")
    robot.expect('The text in the screen vanishes!')

f.close()
f1.close()
