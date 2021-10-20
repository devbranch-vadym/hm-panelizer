# Copyright 2021 HalfMarble LLC

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Final
from kivy.graphics import Color

FIT_SCALE: Final = 0.75

PCB_MASK_COLOR: Final = Color(0.15, 0.35, 0.15, 1.00)
PCB_OUTLINE_COLOR: Final = Color(0.00, 0.00, 0.00, 1.00)
PCB_TOP_PASTE_COLOR: Final = Color(0.55, 0.55, 0.55, 1.00)
PCB_TOP_SILK_COLOR: Final = Color(0.95, 0.95, 0.95, 1.00)
PCB_TOP_MASK_COLOR: Final = Color(0.75, 0.65, 0.00, 1.00)
PCB_TOP_TRACES_COLOR: Final = Color(0.00, 0.50, 0.00, 0.50)
PCB_BOTTOM_TRACES_COLOR: Final = Color(0.00, 0.50, 0.00, 0.50)
PCB_BOTTOM_MASK_COLOR: Final = Color(0.75, 0.65, 0.00, 1.00)
PCB_BOTTOM_SILK_COLOR: Final = Color(0.95, 0.95, 0.95, 1.00)
PCB_PASTE_COLOR: Final = Color(0.55, 0.55, 0.55, 1.00)
PCB_DRILL_NPH_COLOR: Final = Color(0.10, 0.10, 0.10, 0.80)
PCB_DRILL_COLOR: Final = Color(0.10, 0.10, 0.10, 0.90)

PCB_PANEL_GAP_MM: Final = 5
PCB_PANEL_TOP_RAIL_MM: Final = 50
PCB_PANEL_BOTTOM_RAIL_MM: Final = 50
