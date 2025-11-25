// Comprehensive list of all stoppage modifiers from stoppages.grl.
// This file contains all canonical stoppage names with default modifier configurations
// based on the rules defined in internal/rule/common_rules/stoppages.grl.

package stoppages

import (
	"github.com/AbraxaGroup/laytime-agent/internal/model"
)

// DefaultStoppageConfigurations returns a comprehensive map of all stoppage configurations
// with default modifier values as defined in the canonical stoppages.grl rules.
//
//nolint:funlen,maintidx // This is a large configuration function by design.
func DefaultStoppageConfigurations() map[string]model.StoppageConfiguration {
	return map[string]model.StoppageConfiguration{

		// ==========================================
		// 1. NAVIGATION & MOVEMENT
		// Logic: Vessel movement/navigation is generally the Owner's responsibility.
		// If the ship is moving, it is not available to load/discharge.
		// ==========================================
		"MOORING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"UNMOORING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"MANOEUVRING": {
			ModifierUnlessUsed:            0.0, // 0.0: Ship moving/Not at disposal
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(0.0),
			ModifierNotUsedOnDemurrage:    toPtr(0.0),
		},
		"DRIFTING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"PILOTAGE_SUSPENDED": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"PONTOON_SHIFTING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"SHIFTING": {
			ModifierUnlessUsed:            0.0, // 0.0: Navigation/Movement time
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(0.0),
			ModifierNotUsedOnDemurrage:    toPtr(0.0),
		},
		"SHIFTING_BETWEEN_HOLDS": {
			ModifierUnlessUsed:            1.0, // 1.0: Operational shifting requested by cargo usually counts
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"SHIFTING_FROM_WAITING_PLACE": {
			ModifierUnlessUsed:            0.0,
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(0.0),
			ModifierNotUsedOnDemurrage:    toPtr(0.0),
		},
		"SHIFTING_TO_WAITING_PLACE": {
			ModifierUnlessUsed:            0.0,
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(0.0),
			ModifierNotUsedOnDemurrage:    toPtr(0.0),
		},
		"TRANSIT_PASSAGE_INTERRUPTION": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"WARPING": {
			ModifierUnlessUsed:            1.0, // 1.0: Minor shifting alongside usually counts
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},

		// ==========================================
		// 2. WEATHER & ENVIRONMENTAL
		// Logic: Default is 1.0. Weather does not stop time unless contract (CP) has WWD clause.
		// Specific cargo sensitivity is determined by the cargo, not the stoppage default.
		// ==========================================
		"BAD_WEATHER": {
			ModifierUnlessUsed:            1.0, // 1.0: Default time runs (CP overrides this later)
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"EXTREME_TEMPERATURE": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"FOG": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"HAIL": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"HIGH_HUMIDITY": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"HIGH_WINDS": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"HURRICANE": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"ICE": {
			ModifierUnlessUsed:            0.0, // 0.0: Usually Force Majeure / Navigation unsafe
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"RAIN": {
			ModifierUnlessUsed:            1.0, // 1.0: Rain does not stop clock by default
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"ROUGH_SEA": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"SNOW": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"SWELL": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"TORNADO_WARNING": {
			ModifierUnlessUsed:            1.0, // 1.0: Safety stop unless Force Majeure declared
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(0.0),
			ModifierNotUsedOnDemurrage:    toPtr(0.0),
		},
		"WAITING_FOR_FAVORABLE_CONDITIONS": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},

		// ==========================================
		// 3. VESSEL STATUS (Faults, Readiness & Maintenance)
		// Logic: Events preventing the vessel from providing service due to
		// internal issues are Owner's Fault (0.0).
		// ==========================================
		"BUNKERING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               0.0, // 0.0: Ship's business/Not available to Charterer
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"BUNKERING_SUSPENDED": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"CLEANING_HOLDS": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               0.0, // 0.0: Vessel not ready to receive cargo (Owner's risk)
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"CLEANING_LINE": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"CLEANING_TANKS": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               0.0, // 0.0: Vessel not ready
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"MECHANICAL_DELAY": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               0.0, // 0.0: Internal vessel failure
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"REPAIRS": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               0.0, // 0.0: Maintenance is Owner's time
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"SHIP_BREAKDOWN": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               0.0, // 0.0: Owner's fault; Laytime suspended
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(0.0),
		},
		"SHIP_CRANE_BREAKDOWN": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               0.0, // 0.0: Owner failed to provide working gear
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"SHIP_PREPARATION": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               0.0, // 0.0: Vessel preparation is Owner's obligation
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"SHIP_REASONS": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               0.0, // 0.0: Generic Owner fault
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(0.0),
		},
		"VESSEL_BEING_AGROUND": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               0.0, // 0.0: Navigation failure/Owner's risk
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"VESSEL_IN_DETENTION": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               0.0, // 0.0: Legal hold on vessel (Owner's risk)
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"VESSEL_STANDBY_IDLE": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},

		// ==========================================
		// 4. CARGO OPERATIONS (Core)
		// Logic: Standard operations required to move cargo count as Used Laytime (1.0).
		// ==========================================
		"BACKLOADING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"DISCHARGING": {
			ModifierUnlessUsed:            1.0, // 1.0: Core operation
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"DISCHARGING_ANOTHER_CARGO": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"DISCHARGING_STOPPAGE": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"LASHING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"LIGHTERING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"LOADING": {
			ModifierUnlessUsed:            1.0, // 1.0: Core operation
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"LOADING_ANOTHER_CARGO": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"LOADING_FIRST_FOOT": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"LOADING_STOPPAGE": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"SHIP_TO_SHIP_ALIGNMENT": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"TRANSSHIPMENT_IN_PROGRESS": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"TRIMMING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"UNLASHING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},

		// ==========================================
		// 5. CARGO TECHNICAL & PROCEDURES
		// Logic: Steps required to handle the specific cargo type count as 1.0.
		// ==========================================
		"DERATIZATION": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"DISINFECTION": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"DISINSECTION": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"OPERATIONS_STOPPAGE": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"ADDITIVATION": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"ARMS_CONNECTED": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"ARMS_DISCONNECTED": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"BALLAST_HOSE_CONNECTED": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"BALLAST_HOSE_DISCONNECTED": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"BALLASTING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"BILGE_WATER_DISCHARGING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"BLANKETING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"BLOWING_LINES": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"CARGO_CALCULATIONS": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"CARGO_CIRCULATION": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"CARGO_HEATING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"CARGO_MEETING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"CARGO_PARCEL": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"CLOSING_HOLDS": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"CRUDE_OIL_WASHING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"DE_RIGGING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"DEBALLASTING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"DEFENDERING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"DESLOPPING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"DISPOSAL_HOSE_CONNECTED": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"DISPOSAL_HOSE_DISCONNECTED": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"DISPOSAL_IN_PROGRESS": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"DOPING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"FENDERING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"FUMIGATION": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"HOLDS_PREPARATION": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"HOLDS_VENTILATION": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"HOSE_CONNECTED": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"HOSE_DISCONNECTED": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"KNOCKING_DOWN": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"LINE_DISPLACEMENT": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"LINE_FLUSHING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"LINE_SHIFTING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"LINE_UP": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"OPENING_HOLDS": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"PIGGING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"PLACING_CARGO_EQUIPMENT": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"PREPARATION_FOR_CARGO_OPERATIONS": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"PREWASH": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"PURGING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"REFUELLING_SHORE_CRANE": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"REMOVING_CARGO_EQUIPMENT": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"RIGGING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"SAMPLING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"SEALING_HOLDS": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"SEALING_TANKS": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"SHIFT_CHANGE": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"SHIFTING_CARGO": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"SHIFTING_CARGO_EQUIPMENT": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"SHIP_SHORE_LINE_UP_IN_PROGRESS": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"SLUDGE_DISCHARGE": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"SOUNDING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"SQUEEGING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"STRIPPING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"SWEEPING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"TANKS_TREATMENT": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"ULLAGING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"WIRE_DELIVERY_REDELIVERY_IN_PROGRESS": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},

		// ==========================================
		// 6. SURVEYS & INSPECTIONS
		// Logic: Routine surveys required for cargo count (1.0).
		// Rejections or non-routine stops might be 0.0 (if Owner fault),
		// but generally surveys are part of the "used" time.
		// ==========================================
		"BUNKER_SURVEY": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"DRAFT_CHECK": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"DRAFT_SURVEY": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"FINAL_DRAFT_SURVEY": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"GAS_FREE_INSPECTION": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"GAUGING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"HOLD_INSPECTION_REJECTION": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               0.0, // 0.0: Vessel failed inspection (Owner's risk)
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"HOLDS_INSPECTION": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"INITIAL_DRAFT_SURVEY": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"INSPECTION_IN_PROGRESS": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"JOINT_INSPECTION": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"ON_OFF_HIRE_SURVEY": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"SAFETY_INSPECTION": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"SURVEY_IN_PROGRESS": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"TANKS_INSPECTION": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"TANKS_MEASUREMENT": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"USCG_INSPECTION": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},

		// ==========================================
		// 7. WAITING & DELAYS
		// Logic: Waiting for cargo/berth/labor is generally Charterer's risk/commercial delay (1.0).
		// Navigation delays (Tide/Daylight) are Owner's risk (0.0) unless CP says "WIPON".
		// ==========================================
		"CONGESTION": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"VESSEL_ANCHORED": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"WAITING_AT_ANCHORAGE": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"WAITING_AT_ROADS": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"WAITING_BERTH_AVAILABILITY": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"WAITING_FOR_ANALYSIS_RESULTS": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"WAITING_FOR_BARGE": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"WAITING_FOR_CARGO": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"WAITING_FOR_CARGO_OPERATIONS": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"WAITING_FOR_CERTIFICATE": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"WAITING_FOR_COMMENCEMENT_OF_LAYCAN": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"WAITING_FOR_DAYLIGHT": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               0.0, // 0.0: Navigation safety / Owner's risk
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"WAITING_FOR_DOCUMENTS": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"WAITING_FOR_GANGWAY": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"WAITING_FOR_HOLDS_CLEANING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"WAITING_FOR_HOLDS_INSPECTION": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"WAITING_FOR_INSPECTION": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"WAITING_FOR_PILOT": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"WAITING_FOR_REPRESENTATIVE": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"WAITING_FOR_SHIP_SHORE_LINE_UP": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"WAITING_FOR_SHORE_FACILITIES": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"WAITING_FOR_SHORE_LABOR": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"WAITING_FOR_STEVEDORES": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"WAITING_FOR_SURVEYOR": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"WAITING_FOR_TANKS_CLEANING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"WAITING_FOR_TANKS_INSPECTION": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"WAITING_FOR_TIDE": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               0.0, // 0.0: Navigation safety / Owner's risk
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"WAITING_FOR_TRUCKS": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"WAITING_FOR_VESSEL_READINESS": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               0.0, // 0.0: Owner's responsibility
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},

		// ==========================================
		// 8. ADMINISTRATIVE, LEGAL & FORCE MAJEURE
		// Logic: Time runs 24/7 (1.0) unless a "SHEX" clause exists.
		// Force Majeure events stopping the port stop the clock (0.0).
		// ==========================================
		"BREAK": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"CHANNEL_CLOSURE": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"CUSTOMS_FORMALITIES": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"FINANCIAL_HOLD_ON_CARGO": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"FORCE_MAJEURE": {
			ModifierUnlessUsed:            0.0,
			ModifierNotUsed:               0.0, // 0.0: Clock stops
			ModifierUnlessUsedOnDemurrage: toPtr(0.0),
			ModifierNotUsedOnDemurrage:    toPtr(0.0),
		},
		"FREE_PRATIQUE_GRANTING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0, // 0.0: Prerequisite for Laytime to commence
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"HOLIDAY": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0, // 1.0: Continuous time flow (unless CP says SHEX)
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"INWARD_FORMALITIES": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"KEY_MEETING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"LOCK_CLOSURE": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"OPERATIONAL_DELAY": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"OUTWARD_FORMALITIES": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"PORT_CLOSURE": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               0.0, // 0.0: Impossibility to operate
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"PORT_CLOSED": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"QUARANTINE": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               0.0, // 0.0: Vessel legally barred from ops
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"SAFETY_MEETING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"STRIKE_DISCHARGING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"STRIKE_DISCHARGING_TRANSITIONED": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
			//nolint:mnd // Kept for test consistency.
			DemurrageModifier: toPtr(0.5),
		},
		"STRIKE_LOADING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"TIDE_RESTRICTION": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"WEEKEND": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0, // 1.0: Continuous time flow (unless CP says SHEX)
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"WELDING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},

		// ==========================================
		// 9. SHORE & TERMINAL ISSUES
		// Logic: Equipment failure on shore is usually Charterer's risk (1.0).
		// ==========================================
		"BOOMING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"CONVEYOR_BELT_BREAKDOWN": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"ELECTRICAL_DELAY": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"FRESH_WATER_SUPPLYING": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"GANGWAY_UNSAFE": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"SHORE_BREAKDOWN": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0, // 1.0: Charterer's risk
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"SHORE_CRANE_BREAKDOWN": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"SHORE_PREPARATION": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"SHORE_REASONS": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"SUPPLYING_IN_PROGRESS": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"TERMINAL_DOWN_TIME": {
			ModifierUnlessUsed:            1.0,
			ModifierNotUsed:               1.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
	}
}

func toPtr[T any](v T) *T {
	return &v
}
