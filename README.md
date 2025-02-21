# NI VeriStand Real-Time Sequence Example

Example showing how to assign values to variables from an external configuration class in a NI VeriStand real-time sequence.

## Description

This code demonstrates:
- Importing values from an external configuration class
- Creating NI VeriStand variables and channel references 
- Basic variable arithmetic and assignment

## Dependencies

- NI VeriStand
- niveristand Python module
- configClass.py with config_1 class

## Code Example

```python
from niveristand import nivs_rt_sequence, NivsParam, realtimesequencetools
from niveristand.clientapi import *
from niveristand.library import wait
from configClass import config_1

@nivs_rt_sequence
def test():
    # Create variables
    var1 = DoubleValue(config_1.max_val.value) # Get value from config
    var2 = DoubleValue(10)
    
    # Create channel reference
    var5 = ChannelReference(config_1.chann_1)
    
    # Assign sum to channel
    var5.value = var1 + var2
```

## Usage

1. Create configClass.py with required configuration values
2. Import and use configuration values in real-time sequence
3. Run sequence in NI VeriStand environment

## Notes

- Variables must be properly defined in configuration class
- Channel references must point to valid NI VeriStand channels
