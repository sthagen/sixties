# Python-Sixties

Parsing of fixed width text databases derived in the Seventies from the Sixties’ spirit of the previous century.

## What is in it
Probably nothing interest for most visitors.

## To Do

* detect topics as hashes
* avoid intermediate data proofing (duplicated data)
* support with tests (to make data proofing irrelevant)
* align with published hierarchical structures
* enable clear transfer from specs to data classes (or whatever will be used in implementation)
* map parsers to spec aligned names
* explore text based verification like in below Sketch #1

### Sketch #1

```
# 4.1.7.1 Airport Primary Record for KLGA

Recort Type
|Customer/Area Code
||  Section Code
||  |Blank                                              Airport Elevation
||  ||Airport ICAO Identifier                           |    Speed Limit
||  |||   ICAO Code                                     |    |  Recommended Navaid
||  |||   | Subsection Code                             |    |  |   ICAO Code
||  |||   | |ATA/IATA Designator                        |    |  |   | Transistions ALtitude
||  |||   | ||  Reserved                                |    |  |   | |    Transition Level
||  |||   | ||  | Blank                                 |    |  |   | |    |    Public/Military Indicator
||  |||   | ||  | |  Continuation Record Number         |    |  |   | |    |    |Time Zone
||  |||   | ||  | |  |Speed Limit Altitude              |    |  |   | |    |    ||  Daylight Indicator
||  |||   | ||  | |  ||    Longest Runway               |    |  |   | |    |    ||  |Magnetic/True Indicator
||  |||   | ||  | |  ||    |  IFR Capability            |    |  |   | |    |    ||  ||Datum Code
||  |||   | ||  | |  ||    |  |Longest Runway Surface Code   |  |   | |    |    ||  |||  Reserved
||  |||   | ||  | |  ||    |  ||Latitude                |    |  |   | |    |    ||  |||  |   Airport Name
||  |||   | ||  | |  ||    |  |||        Longitude      |    |  |   | |    |    ||  |||  |   |                             File Record No.
||  |||   | ||  | |  ||    |  |||        |         Magnetic Variation |    |    ||  |||  |   |                             |    Cycle Date
||  |||   | ||  | |  ||    |  |||        |         |    |    |  |   | |    |    ||  |||  |   |                             |    |
SUSAP KLGAK6ALGA     110000070Y N40463810W073522140W012000021250LGA K61800018000CR00YMNAR    LAGUARDIA                     133371610
 --- -    -- ---  --- -----   - ---------          -----     ---    --     ----- --- -   ----                              -----
123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012
         1         2         3         4         5         6         7         8         9         10        11        12        132

# 4.1.7.2 Airport Continuation Records for KLGA

Recort Type
|Customer/Area Code
||  Section Code
||  |Blank
||  ||Airport ICAO Identifier
||  |||   ICAO Code
||  |||   | Subsection Code
||  |||   | |ATA/IATA Designator
||  |||   | ||  Reserved
||  |||   | ||  | Blank
||  |||   | ||  | |  Continuation Record Number
||  |||   | ||  | |  |Application Type
||  |||   | ||  | |  ||Notes
||  |||   | ||  | |  |||
||  |||   | ||  | |  |||
||  |||   | ||  | |  |||                                                                    Reserved
||  |||   | ||  | |  |||                                                                    |                              File Record No.
||  |||   | ||  | |  |||                                                                    |                              |    Cycle Date
||  |||   | ||  | |  |||                                                                    |                              |    |
SUSAP KLGAK6ALGA     2JNEW YORK                NYUSA              DKJFKK6NNNYNNNNYNNNNNNYYYYNNYY  Y0000YYYP          1YR00Y133381610
 --- -    -- ---  --- -                                                                     -------------------------------     ----
123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012
         1         2         3         4         5         6         7         8         9         10        11        12        132

```
