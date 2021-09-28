Introduction
============

Serialization is a library from **boost** offering the possibility to
serialize / deserialize objects to C ++ ascii text files, XML or binary
format.

Its main advantages are:

-  Requires very little change in the object code to serialize, if the
   code is unmodifiable (p. eg. QString) the object can be serialized
   unobtrusively.

-  We have serialization in ascii, xml and binary format with *dump* for
   traces automatically.

-  We can serialize objects that contain pointers, stl containers or are
   derived without additional modifications.

-  It Supports the possibility of versions to ensure compatibility.

The library is not implemented only with *includes* so, it is necessary
to compile and include it in the assembly.

Installation
------------

In the directory:

::

    c:\workcopy\extsw\noarch\boost_1_49_0

We use the command:

::

    bootstrap.bat

This command generates the b2.exe program and using it we get the
libraries:

::

     Directory of c:\workcopy\extsw\noarch\boost_1_49_0\stage\lib

    30/03/2016  12:58        11.650.918 libboost_serialization-vc100-mt-1_49.lib
    30/03/2016  12:49        30.476.976 libboost_serialization-vc100-mt-gd-1_49.lib
    30/03/2016  12:58         9.001.158 libboost_wserialization-vc100-mt-1_49.lib
    30/03/2016  12:49        20.677.776 libboost_wserialization-vc100-mt-gd-1_49.lib       

We are going to use the first one compiled without debug information.

Additionally we use the file *simple\_log\_archive.hpp* to get log info
from entities with serialization enabled.

Use examples
============

Modification to make a class serializable
-----------------------------------------

We have to create a private method *serialize* where we include the
variables defining the class and make the class friend of

::

    boost::serialization::access

.. code:: cpp

    #include <boost/archive/xml_oarchive.hpp>
    #include <boost/archive/xml_iarchive.hpp>
    #include <boost/archive/text_oarchive.hpp>
    #include <boost/archive/text_iarchive.hpp>
    #include <boost/serialization/vector.hpp>
    #include <fstream>
    #include "simple_log_archive.hpp"
    #include <string>

    class ForanPart
    {
    public:
      ForanPart( std::string name, int thickness, float weight): _name(name), 
      _thickness(thickness), _weight(weight) {}
      ForanPart(){}
    private:

      friend class boost::serialization::access;
      std::string _name;
      int _thickness;
      float _weight;

      template<class Archive>
      void serialize(Archive & ar, const unsigned int /*version*/)
      {
        ar & BOOST_SERIALIZATION_NVP(_name);
        ar & BOOST_SERIALIZATION_NVP(_thickness);
        ar & BOOST_SERIALIZATION_NVP(_weight);
      }
    };

Serialization/deserialization to ascii file
-------------------------------------------

With the following code we can save and read from/to an ascii file

.. code:: cpp

    std::ofstream ofs("part_file_1.txt"); 
    boost::archive::text_oarchive ar(ofs); 
    ar & BOOST_SERIALIZATION_NVP(part_1); 


Serialization/deserialization to xml file
-----------------------------------------

Just changing text_oarchive, text_iarchive by xml_oarchive,
xml_iarchive we get serialization to/from xml.

The result is:

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
    <!DOCTYPE boost_serialization>
    <boost_serialization signature="serialization::archive" version="9">
    <part_1 class_id="0" tracking_level="0" version="0">
            <_name>part_1</_name>
            <_thickness>2</_thickness>
            <_weight>3.4000001</_weight>
    </part_1>
    </boost_serialization>

Log for a serializable entity
-----------------------------

Once the serialization is implemented we can get a log from this entity
with the code:

.. code:: cpp

      ForanPart part_1("part_1", 2, 3.4f);

      simple_log_archive log(std::cout);
      log << part_1;

The result in the console is: ~\ :sub:`~` \_name part\_1 \_thickness 2
\_weight 3.4 ~\ :sub:`~`

STL containers serialization
----------------------------

If we have a member to serialize that is an STL container we don't have
to add additional code, the behavior is managed by the library like a
primitive type ( int, float...)

.. code:: cpp

    class ForanPart
    {
    public:
      ForanPart( std::string name, int thickness, float weight): _name(name), 
      _thickness(thickness), _weight(weight) 
      {
        _pcp.push_back(0);
        _pcp.push_back(0);
        _pcp.push_back(999999);
        _pcp.push_back(999999);
        _pcp.push_back(1);
        _pcp.push_back(1);
      }
      ForanPart(){}
    private:

      friend class boost::serialization::access;
      std::string _name;
      int _thickness;
      float _weight;
      std::vector<float> _pcp;

      template<class Archive>
      void serialize(Archive & ar, const unsigned int /*version*/)
      {
        ar & BOOST_SERIALIZATION_NVP(_name);
        ar & BOOST_SERIALIZATION_NVP(_thickness);
        ar & BOOST_SERIALIZATION_NVP(_weight);
        ar & BOOST_SERIALIZATION_NVP(_pcp);
      }
    };

We get:

::

    part_file_1.txt

    22 serialization::archive 9 0 0 6 part_1 2 3.4000001 6 0 0 0 999999 999999 1 1

    part_file_2.xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
    <!DOCTYPE boost_serialization>
    <boost_serialization signature="serialization::archive" version="9">
    <part_1 class_id="0" tracking_level="0" version="0">
            <_name>part_1</_name>
            <_thickness>2</_thickness>
            <_weight>3.4000001</_weight>
            <_pcp>
                    <count>6</count>
                    <item_version>0</item_version>
                    <item>0</item>
                    <item>0</item>
                    <item>999999</item>
                    <item>999999</item>
                    <item>1</item>
                    <item>1</item>
            </_pcp>
    </part_1>
    </boost_serialization>

    log

    _name part_1
    _thickness 2
    _weight 3.4
    _pcp
     count 6
     item_version 0
     item 0
     item 0
     item 999999
     item 999999
     item 1
     item 1

Serialization for external entities
===================================

QString
-------

In this case we implement some auxiliary functions, in the case of a
QString:

.. code:: cpp

    #ifndef QSTRINGSERIALIZER_H
    #define QSTRINGSERIALIZER_H
     
    namespace boost {
        namespace serialization {
     
         template<class Archive>
         void save( Archive & ar, const QString& qStringParam, const unsigned int )
         {
             // save class member variables
             std::string stdString = qStringParam.toStdString();
             ar & BOOST_SERIALIZATION_NVP(stdString);
         }

         template<class Archive>
         void load( Archive & ar, QString& qStringParam, const unsigned int )
         {
             // load class member variables
             std::string stdString;
             ar & BOOST_SERIALIZATION_NVP(stdString);
             qStringParam = qStringParam.fromStdString(stdString);
         }

         template<class Archive>
         void serialize(Archive & ar, QString & t, const unsigned int file_version)
         {
             split_free(ar, t, file_version);
         }

     } // namespace serialization
    } // namespace boost
    #endif // QSTRINGSERIALIZER_H

An example of class with a QString to serialize is:

.. code:: cpp

    #ifndef USER_H
    #define USER_H
     
    class User
    {
    public:
     
        User() {}
     
        User(const QString &name, const QString &surname)
        {
            this->name = name;
            this->surname = surname;
        }
     
        QString getName() { return name; }
        QString getSurname() { return surname; }
     
    private:
        QString name;
        QString surname;
     
        friend class boost::serialization::access;
        template<class Archive>
        void serialize(Archive & ar, const unsigned int version)
        {
            // serialize deserialize QString instance variables
            ar & BOOST_SERIALIZATION_NVP(name);
            ar & BOOST_SERIALIZATION_NVP(surname);
        }
     
    };
     
    #endif // USER_H

And one use examples is:

.. code:: cpp

    #include <boost/archive/xml_iarchive.hpp>
    #include <boost/archive/xml_oarchive.hpp>
    #include <boost/serialization/string.hpp>
    #include <boost/serialization/nvp.hpp>
     
    #include <QString>
    #include <fstream>
    #include <iostream>
     
    #include "User.h"
    #include "QStringSerializer.h"
     
    using namespace std;
     
    int main()
    {
      {
          // Initialize User object to serialize with data
          User user("userName","userSurname");
          std::ofstream ofs("stateInfoFile.xml");
          boost::archive::xml_oarchive oa(ofs);
          // write class instance to archive
          oa & BOOST_SERIALIZATION_NVP(user);
      }

      {
          User user;
          std::ifstream ifs("stateInfoFile.xml");
          boost::archive::xml_iarchive ia(ifs);
          // read class instance back from archive
          ia & BOOST_SERIALIZATION_NVP(user);

          std::cout << "Name : " << user.getName().toStdString() << std::endl;
          std::cout << "Surname : " << user.getSurname().toStdString() << std::endl;
      }
    }

TopoDS\_Shape
-------------

The implementation in the case of a TopoDS\_Shape is the following, by
inheritance it is available to the derived classes.

.. code:: cpp

    namespace boost {
      namespace serialization {

        template <class Archive> 
        void save (Archive & ar, const TopoDS_Shape& shape, const unsigned int )
        {
          std::ostringstream ostr;
          BRepTools::Write(shape, ostr);
          std::string stdstring = ostr.str();
          ar & BOOST_SERIALIZATION_NVP(stdstring);
        }

        template <class Archive>
        void load(Archive & ar, TopoDS_Shape& shape, const unsigned int)
        {
          std::string stdstring;
          ar & BOOST_SERIALIZATION_NVP(stdstring);
          std::istringstream istr(stdstring);
          BRep_Builder aBuilder;
          BRepTools::Read(shape, istr, aBuilder);
        }

        template <class Archive>
        void serialize(Archive & ar, TopoDS_Face & face, const unsigned int file_version)
        {
          split_free(ar, face, file_version);
        }
      }
    }

Example of use:

.. code:: cpp

    class ForanPart
    {
    public:
      ForanPart( std::string name, int thickness, float weight): _name(name), 
        _thickness(thickness), _weight(weight) 
      {
        _pcp.push_back(0);
        _pcp.push_back(0);
        _pcp.push_back(999999);
        _pcp.push_back(999999);
        _pcp.push_back(1);
        _pcp.push_back(1);

        _face = OCTestTools::ProfileFace("X 2 Y 1 X -2");
      }
      ForanPart() {}

      void WriteFaceBrep()
      {
        BRepTools::Write(_face, "boost_face.brep");
      }
    private:

      friend class boost::serialization::access;
      std::string _name;
      int _thickness;
      float _weight;
      std::vector<float> _pcp;
      TopoDS_Face _face;

      template<class Archive>
      void serialize(Archive & ar, const unsigned int /*version*/)
      {
        ar & BOOST_SERIALIZATION_NVP(_name);
        ar & BOOST_SERIALIZATION_NVP(_thickness);
        ar & BOOST_SERIALIZATION_NVP(_weight);
        ar & BOOST_SERIALIZATION_NVP(_pcp);
        ar & BOOST_SERIALIZATION_NVP(_face);
      }
    };

.. code:: cpp

    TEST(BoostSerializationTest, boost_serialize_sample_xml)
    {
      {
        ForanPart part_1("part_1", 2, 3.4f);
        std::ofstream ofs("part_file_2.xml");
        boost::archive::xml_oarchive ar(ofs);
        ar & BOOST_SERIALIZATION_NVP(part_1);
      }

      {
        ForanPart part_2;
        std::ifstream ifs("part_file_2.xml");
        boost::archive::xml_iarchive ar(ifs);
        ar & BOOST_SERIALIZATION_NVP(part_2);
        part_2.WriteFaceBrep();
      }
    }

The output is:

.. code:: xml

     1 <?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
     2 <!DOCTYPE boost_serialization>
     3 <boost_serialization signature="serialization::archive" version="9">
     4 <part_1 class_id="0" tracking_level="0" version="0">
     5   <_name>part_1</_name>
     6   <_thickness>2</_thickness>
     7   <_weight>3.4000001</_weight>
     8   <_pcp>
     9     <count>6</count>
    10     <item_version>0</item_version>
    11     <item>0</item>
    12     <item>0</item>
    13     <item>999999</item>
    14     <item>999999</item>
    15     <item>1</item>
    16     <item>1</item>
    17   </_pcp>
    18   <_face class_id="2" tracking_level="0" version="0">
    19     <stdstring>
    20 CASCADE Topology V1, (c) Matra-Datavision
    21 Locations 0
    22 Curve2ds 0
    23 Curves 4
    24 1 0 0 0 1 0 0
    25 1 2 0 0 0 1 0
    26 1 2 1 0 -1 -0 0
    27 1 0 1 0 0 -1 -0
    28 Polygon3D 0

Common errors
-------------

If we get the error:

::

    terminate called after throwing an instance of 'boost::archive::archive_exception' 
    what(): invalid signature
    Aborted

We must check that we have active only one of the two entities

boost::archive::text\_oarchive or boost::archive::text\_iarchive

at the same time.

Utilities
---------

We collect the needed utilities to be used in serialization in the
include:

``BoostSerializationUtils.h``

Full serialization example
==========================

As a real use example we will provide a full serialization
implementation for the ``AnaSurfPlateUnfolding`` class. This class is
used to calculate the expanded geometry for plate defined on an
analytical surface (extrusion or corrugated).

The class is defined in ``geotools/AnaSurfPlateUnfolding.h`` and we'll
use also an instance of the class ``LinearExtrusionSurfaceTools``
defined in ``geotools/LinearExtrusionSurfaceTools.h``

We make serializable every component needed:

.. code:: cpp

     struct PlateContours
     {
       TopoDS_Wire outer;
       std::vector<TopoDS_Wire> holes;
       std::vector<TopoDS_Wire> markings;

       friend class boost::serialization::access;
       template<class Archive>
       void serialize(Archive & ar, const unsigned int /*version*/)
       {
         ar & BOOST_SERIALIZATION_NVP(outer);
         ar & BOOST_SERIALIZATION_NVP(holes);
         ar & BOOST_SERIALIZATION_NVP(markings);
       }
     };

Now we can make serializable ``AnaSurfPlateUnfolding`` with the code

.. code:: cpp

    private:
      LinearExtrusionSurfaceTools _linear_extr_surf_tools;
      PlateContours _plate_contours;

      ....
      
      friend class boost::serialization::access;
      template<class Archive>
      void serialize(Archive & ar, const unsigned int /*version*/)
      {
        ar & BOOST_SERIALIZATION_NVP(_linear_extr_surf_tools);
        ar & BOOST_SERIALIZATION_NVP(_plate_contours);
      }

Because ``PlateConstours`` and ``LinearExtrusionSurfaceTools`` are
already serializable entities.

An example of use is the following unit test located in
``geotools/test/AnaSurfPlateUnfoldingTest.cpp``:

.. code:: cpp

    TEST(AnaSurfPlateUnfoldingTest, boost_serialization)
    {
      {
        TopoDS_Wire profile = OCTestTools::ProfileOpenWire("X 2 X 4");
        LinearExtrusionSurfaceTools LES(profile, gp_Vec(0, 4, 0));

        PlateContours plate_contours;
        plate_contours.outer = OCTestTools::ProfileClosedWire("X 4 Y 3 X -4");
        plate_contours.holes.push_back(OCTestTools::ProfileClosedWire("F 1 1 X 1 Y 1 X -1"));
        plate_contours.markings.push_back(OCTestTools::ProfileOpenWire("F 3 1 Y 1"));

        AnaSurfPlateUnfolding ana_surf_plt_unfold(LES);
        ana_surf_plt_unfold.LoadPlateContours(plate_contours);

        SaveToXML(ana_surf_plt_unfold, "T_aspu.xml");
        SaveToTxt(ana_surf_plt_unfold, "T_aspu.txt");
     
        AnaSurfPlateUnfolding ana_surf_plt_unfold3;
        LoadFromXML(ana_surf_plt_unfold3, "T_aspu.xml");

        AnaSurfPlateUnfolding ana_surf_plt_unfold4;
        LoadFromTxt(ana_surf_plt_unfold4, "T_aspu.txt");
      }
    }

Using the test program we get:

::

    c:\workcopy\ForanDesa\src\geotools\test>windows_x86\geotools_test.exe --gtest_filter=AnaSurfPlate*
    Running main() from gtest_main.cc
    Note: Google Test filter = AnaSurfPlate*
    [==========] Running 5 tests from 1 test case.
    [----------] Global test environment set-up.
    [----------] 5 tests from AnaSurfPlateUnfoldingTest
    [ RUN      ] AnaSurfPlateUnfoldingTest.planar_square_wire_on_planar_face
    [       OK ] AnaSurfPlateUnfoldingTest.planar_square_wire_on_planar_face (120 ms)
    [ RUN      ] AnaSurfPlateUnfoldingTest.square_wire_on_two_planar_face
    [       OK ] AnaSurfPlateUnfoldingTest.square_wire_on_two_planar_face (10 ms)
    [ RUN      ] AnaSurfPlateUnfoldingTest.square_wire_on_two_faces
    [       OK ] AnaSurfPlateUnfoldingTest.square_wire_on_two_faces (10 ms)
    [ RUN      ] AnaSurfPlateUnfoldingTest.planar_square_wire_on_planar_faces_with_holes_and_markings
    [       OK ] AnaSurfPlateUnfoldingTest.planar_square_wire_on_planar_faces_with_holes_and_markings (10 ms)
    [ RUN      ] AnaSurfPlateUnfoldingTest.boost_serialization
    [       OK ] AnaSurfPlateUnfoldingTest.boost_serialization (10 ms)
    [----------] 5 tests from AnaSurfPlateUnfoldingTest (160 ms total)

    [----------] Global test environment tear-down
    [==========] 5 tests from 1 test case ran. (160 ms total)
    [  PASSED  ] 5 tests.

And we get two files with the serialized entities:

::

    09/06/2016  10:40             2.220 T_aspu.txt
    09/06/2016  10:40             3.152 T_aspu.xml
