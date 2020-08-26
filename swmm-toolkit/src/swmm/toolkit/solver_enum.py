#
#  output_enum.py -
#
#  Created: August 20, 2020
#  Updated:
#
#  Author:     Michael E. Tryby
#              US EPA - ORD/CESER
#              Jennifer Wu
#              Xylem Inc.

#
# Solver API Enums
#

from aenum import Enum, IntEnum


class UnitSystem(Enum, start=0):
    US
    SI


class FlowUnits(Enum, start=0):
    CFS
    GPM
    MGD
    CMS
    LPS
    MLD


class ConcUnits(Enum, start=0):
    MG,
    UG,
    COUNT
    NONE


class NodeType(Enum, start=0):
    JUNCTION
    OUTFALL
    STORAGE
    DIVIDER


class LinkType(Enum, start=0):
    CONDUIT
    PUMP
    ORIFICE
    WEIR
    OUTLET


class LinkDirection(Enum):
    UPSTREAM_TO_DOWNSTREAM = 1
    DOWNSTREAM_TO_UPSTREAM = -1
    
#
# Solver Toolkit API Enums
#

class ObjectProperty(Enum, start=0):
    GAGE
    SUBCATCH 
    NODE
    LINK  
    POLLUT
    LAND_USE 
    TIME_PATTERN
    CURVE
    TIMESERIES   
    CONTROL
    TRANSECT
    AQUIFER
    UNIT_HYD  
    SNOW_MELT
    SHAPE
    LID

    
class TimeProperty(Enum, start=0):
    START_DATE
    END_DATE
    REPORT_DATE


class UnitProperty(Enum, start=0):
    SYSTEM_UNIT
    FLOW_UNIT


class SimOption(Enum, start=0):
    ALLOW_POND
    SKIP_STEADY
    IGNORE_RAIN
    IGNORE_RDII
    IGNORE_SNOW
    IGNORE_GW
    IGNORE_ROUTE
    IGNORE_ROUTE_QUALITY


class SimSetting(Enum, start=0):
    ROUTE_STEP
    MIN_ROUTE_STEP
    LENGTH_STEP
    START_DRY_DAYS
    COURANT_FACTOR
    MIN_SURFACE_AREA
    MIN_SLOPE
    RUNOFF_ERROR
    GW_ERROR
    FLOW_ERROR
    QUALITY_ERROR
    HEAD_TOLERANCE
    SYSTEM_FLOW_TOLERANCE
    LATERAL_FLOW_TOLERANCE


class NodeProperty(Enum, start=0):
    INVERT_ELEVATION
    FULL_DEPTH
    SURCHARGE_DEPTH
    POND_AREA
    INITIAL_DEPTH


class NodeResult(Enum, start=0):
    TOTAL_INFLOW
    TOTAL_OUTFLOW
    LOSSES
    VOLUME
    FLOOD
    DEPTH
    HEAD
    LATERAL_INFLOW

    
class LinkProperty(Enum, start=0):
    OFFSET_1
    OFFSET_2
    INITIAL_FLOW
    FLOW_LIMIT
    INLET_LOSS
    OUTLET_LOSS
    AVERAGE_LOSS


class LinkResult(Enum, start=0):
    FLOW
    DEPTH
    VOLUME
    US_SURFACE_AREA
    DS_SURFACE_AREA
    SETTING
    TARGET_SETTING
    FROUDE

    
class SubcatchProperty(Enum, start=0):
    WIDTH
    AREA
    IMPERVIOUS_FRACTION
    SLOPE
    CURB_LENGTH


class SubcatchResult(Enum, start=0):
    RAIN
    EVAPORATION
    INFILTRATION
    RUNON
    RUNOFF
    SNOW

    
class LidUsageProperty(Enum, start=0):
    UNIT_AREA
    TOP_WIDTH
    BOTTOM_WIDTH
    INITIAL_SATURATION
    FROM_IMPERVIOUS
    FROM_PERVIOUS


class LidUsageOption(Enum, start=0):
    INDEX
    NUMBER
    TO_PERV
    DRAIN_SUBCATCH
    DRAIN_NODE


class LidLayer(Enum, start=0):
    SURFACE
    SOIL
    STORAGE
    PAVEMENT
    DRAIN
    DRAIN_MAT

    
class LidLayerProperty(Enum, start=0):
    THICKNESS
    VOID_FRACTION
    ROUGHNESS
    SURFACE_SLOPE
    SIDE_SLOP
    ALPHA
    POROSITY
    FIELD_CAPACITY
    WILTING_POINT
    SUCTION_HEAD
    K_SATURATION
    K_SLOPE
    CLOG_FACTOR
    IMPERVIOUS_FRACTION
    DRAIN_COEFFICIENT
    DRAIN_EXPONENT
    DRAIN_OFFSET
    DRAIN_DELAY
    DRAIN_HEAD_OPEN
    DRAIN_HEAD_CLOSE
    DRAIN_CURVE
    DRAIN_REGEN_DAYS
    DRAIN_REGEN_DEGREE
    
    
    
    