#include <cstdlib>
#include <iostream>
using namespace std;

int main() {
    system("read -p 'Press Enter to continue...'");
    system("sudo rm -rf /usr/cwplus/");
    system("sudo mkdir /usr/cwplus");
    system("sudo git clone https://github.com/VPeti1/CW_Plus.git /usr/cwplus");
    system("sudo g++ /usr/cwplus/run.cpp -o /usr/bin/cwplus");
    system("sudo chmod +x /usr/bin/cwplus");
    system("sudo rm -r /usr/cwplus/chococ.cpp /usr/cwplus/chococ.exe /usr/cwplus/flex.pkg /usr/cwplus/LICENSE /usr/cwplus/README.md /usr/cwplus/.gitignore");
    std::cout << "Please rerun the program!\n";
}
