#ifndef _io_h_
#define _io_h_
#include <sstream>
#include <string>
#include <iostream>
#include <valarray>
#include <fstream>
#include <vector>


class FileLoader
{
	std::istringstream stream1;
	std::ifstream FileStream;
	int column;
	int row;
	void offsetReader();
  public:
	FileLoader(const std::string &s, int _i = 4, int _j = 2);
	bool FillDataStruct(std::string&,std::vector<float>&,int&);
};

#endif
