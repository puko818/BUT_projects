#include <fstream>
#include <vector>
#include <string>
#include "io.h"


FileLoader::FileLoader(const std::string &s, int _i, int _j) :
	FileStream(s.c_str()), column(_i),row(_j)
{
	offsetReader();
}

void FileLoader::offsetReader()
{
	for (int i = 0; i < row; i++)
	{
		std::string tmp;
		getline(FileStream,tmp);

	}


}

bool FileLoader::FillDataStruct(std::string &name,std::vector<float> &v,int &nodata)
{

    int no_data_count = 0;
	std::string line;
	std::string tmp_flush;
	int n=0,i = 0;
	float num = 0.0;
	bool done = true;
	if (getline(FileStream,line) && line.size())
	{
		stream1.clear();
    	stream1.str(line);
    	stream1 >> name;
		//std::cout << d.name << std::endl;
    	for (int i = 0; i < column; i++)
    	{
    		getline(stream1,tmp_flush,'\t');
    	}
    	while (stream1 >> num)
    	{
    		n = stream1.tellg();
    		v.push_back(num);
    		/*ked je vynechana nejaka hodnota, vloz neumerne male cislo*/
    		if (line[n] == '\t' && line[n+1] == '\t')
    		{
    					v.push_back(-100.0);
    					no_data_count++;
    		}
    	 //   std::cout << v[i] << std::endl;
    	}


	}
	else done = false;
	nodata = no_data_count;
	return done;
}


/*
int main()
{
	FileLoader *loader = new FileLoader("fig1.txt",4,2);
	std::string name;
	std::vector<float> v;

	if(loader->FillDataStruct(name,v))
	{

	}
	std::cout << name << std::endl;
	for (std::vector<float>::iterator I = v.begin(); I != v.end(); I++)
	{
        std::cout << *I << std::endl;

	}
    std::cout << std::endl;
}
*/
