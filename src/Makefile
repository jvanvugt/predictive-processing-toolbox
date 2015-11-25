CXX= g++
CXXFILESb= LibPCTBuildNetwork.cpp
CXXINTERMEDIATEb= LibPCTBuildNetwork.o
CXXOUTPUTLIBSb= LibPCTBuildNetwork.so
CXXFILESr= LibPCTReadNetwork.cpp
CXXINTERMEDIATEr= LibPCTReadNetwork.o
CXXOUTPUTLIBSr= LibPCTReadNetwork.so
CXXFILESi= LibPCTInference.cpp
CXXINTERMEDIATEi= LibPCTInference.o
CXXOUTPUTLIBSi= LibPCTInference.so
CXXFLAGS= -O3 -DNDEBUG -ffast-math -Wall -fPIC
LIBS = -L./smile/ -lsmile
all: lib
lib:
	$(CXX) $(CXXFLAGS) $(LIBS) -c $(CXXFILESb)
	$(CXX) -shared -o $(CXXOUTPUTLIBSb) $(CXXINTERMEDIATEb) $(LIBS)
	$(CXX) $(CXXFLAGS) $(LIBS) -c $(CXXFILESr)
	$(CXX) -shared -o $(CXXOUTPUTLIBSr) $(CXXINTERMEDIATEr) $(LIBS)
	$(CXX) $(CXXFLAGS) $(LIBS) -c $(CXXFILESi)
	$(CXX) -shared -o $(CXXOUTPUTLIBSi) $(CXXINTERMEDIATEi) $(LIBS)
