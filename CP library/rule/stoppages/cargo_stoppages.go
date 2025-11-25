// Cargo-specific stoppage modifiers based on operational logic for cargo handling.
// This file contains stoppage configurations optimized for cargo operations
// where the primary concern is whether events physically prevent cargo loading/discharging.

package stoppages

import (
	"github.com/AbraxaGroup/laytime-agent/internal/model"
)

// CargoStoppageConfigurations returns a comprehensive map of stoppage configurations
// optimized for cargo operations, focusing on events that physically prevent cargo handling.
func CargoStoppageConfigurations() map[string]model.StoppageConfiguration {
	configs := make(map[string]model.StoppageConfiguration)

	// Add all configuration categories
	addCargoWeatherEvents(configs)
	addCargoEquipmentBreakdowns(configs)
	addCargoLaborIssues(configs)
	addCargoLogisticalIssues(configs)
	addCargoSafetyAndRegulatory(configs)
	addCargoAdministrativeIssues(configs)
	addCargoOperationalPreparations(configs)
	addCargoSpecificOperations(configs)
	addCargoWaitingPeriods(configs)

	return configs
}

// addCargoWeatherEvents adds weather-related cargo stoppage configurations.
//
//nolint:funlen // Configuration function with weather event definitions.
func addCargoWeatherEvents(configs map[string]model.StoppageConfiguration) {
	weatherEvents := map[string]model.StoppageConfiguration{
		"RAIN": {
			ModifierUnlessUsed:            1.0, // Rain can damage cargo and create unsafe working conditions
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"HIGH_WINDS": {
			ModifierUnlessUsed:            1.0, // High winds create safety risks for cargo handling
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"ROUGH_SEA": {
			ModifierUnlessUsed:            1.0, // Rough seas prevent safe cargo transfer operations
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"FOG": {
			ModifierUnlessUsed:            1.0, // Fog reduces visibility and creates safety hazards
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"SNOW": {
			ModifierUnlessUsed:            1.0, // Snow covers equipment and creates hazardous conditions
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"HAIL": {
			ModifierUnlessUsed:            1.0, // Hail can damage cargo and equipment
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"HURRICANE": {
			ModifierUnlessUsed:            1.0, // Hurricanes prevent all cargo operations
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"EXTREME_TEMPERATURE": {
			ModifierUnlessUsed:            1.0, // Extreme temperatures can damage cargo or prevent safe operations
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"HIGH_HUMIDITY": {
			ModifierUnlessUsed:            1.0, // High humidity can affect cargo quality and handling
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"SWELL": {
			ModifierUnlessUsed:            1.0, // Swell affects vessel stability during cargo operations
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"TORNADO_WARNING": {
			ModifierUnlessUsed:            1.0, // Tornado warnings halt all operations for safety
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"ICE": {
			ModifierUnlessUsed:            1.0, // Ice conditions prevent cargo operations
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
	}

	for k, v := range weatherEvents {
		configs[k] = v
	}
}

// addCargoEquipmentBreakdowns adds equipment breakdown cargo stoppage configurations.
//
//nolint:dupl // Similar structure to other configuration functions is intentional.
func addCargoEquipmentBreakdowns(configs map[string]model.StoppageConfiguration) {
	equipmentBreakdowns := map[string]model.StoppageConfiguration{
		"SHORE_BREAKDOWN": {
			ModifierUnlessUsed:            1.0, // Shore equipment failure prevents cargo operations
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"SHIP_CRANE_BREAKDOWN": {
			ModifierUnlessUsed:            1.0, // Ship's cranes are essential for cargo handling
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"SHORE_CRANE_BREAKDOWN": {
			ModifierUnlessUsed:            1.0, // Shore cranes are essential for cargo handling
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"CONVEYOR_BELT_BREAKDOWN": {
			ModifierUnlessUsed:            1.0, // Conveyor systems are critical for cargo flow
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"TERMINAL_DOWN_TIME": {
			ModifierUnlessUsed:            1.0, // Terminal equipment unavailable prevents operations
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"MECHANICAL_DELAY": {
			ModifierUnlessUsed:            1.0, // Mechanical issues prevent cargo handling
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"ELECTRICAL_DELAY": {
			ModifierUnlessUsed:            1.0, // Electrical failures affect cargo equipment
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
	}

	for k, v := range equipmentBreakdowns {
		configs[k] = v
	}
}

// addCargoLaborIssues adds labor and workforce issue cargo stoppage configurations.
func addCargoLaborIssues(configs map[string]model.StoppageConfiguration) {
	laborIssues := map[string]model.StoppageConfiguration{
		"STRIKE_LOADING": {
			ModifierUnlessUsed:            1.0, // No labor available for loading operations
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"STRIKE_DISCHARGING": {
			ModifierUnlessUsed:            1.0, // No labor available for discharging operations
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"WAITING_FOR_STEVEDORES": {
			ModifierUnlessUsed:            1.0, // Essential labor not available for cargo handling
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"WAITING_FOR_SHORE_LABOR": {
			ModifierUnlessUsed:            1.0, // Shore labor essential for cargo operations
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"SHIFT_CHANGE": {
			ModifierUnlessUsed:            1.0, // Shift changes interrupt cargo operations
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"BREAK": {
			ModifierUnlessUsed:            1.0, // Labor breaks interrupt cargo handling
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
	}

	for k, v := range laborIssues {
		configs[k] = v
	}
}

// addCargoLogisticalIssues adds logistical issue cargo stoppage configurations.
func addCargoLogisticalIssues(configs map[string]model.StoppageConfiguration) {
	logisticalIssues := map[string]model.StoppageConfiguration{
		"WAITING_FOR_TRUCKS": {
			ModifierUnlessUsed:            1.0, // No transport available for cargo movement
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"WAITING_FOR_BARGE": {
			ModifierUnlessUsed:            1.0, // Barge transport not available for cargo
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"WAITING_FOR_CARGO": {
			ModifierUnlessUsed:            1.0, // Cargo not ready prevents operations
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"FINANCIAL_HOLD_ON_CARGO": {
			ModifierUnlessUsed:            1.0, // Payment issues prevent cargo movement
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"WAITING_FOR_ANALYSIS_RESULTS": {
			ModifierUnlessUsed:            1.0, // Cargo analysis required before handling
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"WAITING_FOR_CERTIFICATE": {
			ModifierUnlessUsed:            1.0, // Required certificates prevent cargo operations
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
	}

	for k, v := range logisticalIssues {
		configs[k] = v
	}
}

// addCargoSafetyAndRegulatory adds safety and regulatory issue cargo stoppage configurations.
//
//nolint:dupl // Similar structure to other configuration functions is intentional.
func addCargoSafetyAndRegulatory(configs map[string]model.StoppageConfiguration) {
	safetyAndRegulatory := map[string]model.StoppageConfiguration{
		"QUARANTINE": {
			ModifierUnlessUsed:            1.0, // Health restrictions prevent cargo operations
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"PORT_CLOSURE": {
			ModifierUnlessUsed:            1.0, // Port closure prevents all cargo operations
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"CHANNEL_CLOSURE": {
			ModifierUnlessUsed:            1.0, // Navigation restrictions prevent access
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"GANGWAY_UNSAFE": {
			ModifierUnlessUsed:            1.0, // Unsafe access prevents cargo operations
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"HOLD_INSPECTION_REJECTION": {
			ModifierUnlessUsed:            1.0, // Rejected holds prevent cargo loading
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"VESSEL_IN_DETENTION": {
			ModifierUnlessUsed:            1.0, // Detained vessel cannot handle cargo
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"FORCE_MAJEURE": {
			ModifierUnlessUsed:            1.0, // Force majeure events prevent cargo operations
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
	}

	for k, v := range safetyAndRegulatory {
		configs[k] = v
	}
}

// addCargoAdministrativeIssues adds administrative issue cargo stoppage configurations.
func addCargoAdministrativeIssues(configs map[string]model.StoppageConfiguration) {
	administrativeIssues := map[string]model.StoppageConfiguration{
		"CUSTOMS_FORMALITIES": {
			ModifierUnlessUsed:            1.0, // Administrative paperwork doesn't prevent physical operations
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"HOLIDAY": {
			ModifierUnlessUsed:            1.0, // Workforce scheduling doesn't prevent physical operations
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"WEEKEND": {
			ModifierUnlessUsed:            1.0, // Workforce scheduling doesn't prevent physical operations
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
	}

	for k, v := range administrativeIssues {
		configs[k] = v
	}
}

// addCargoOperationalPreparations adds operational preparation cargo stoppage configurations.
func addCargoOperationalPreparations(configs map[string]model.StoppageConfiguration) {
	operationalPreparations := map[string]model.StoppageConfiguration{
		"CLEANING_HOLDS": {
			ModifierUnlessUsed:            1.0, // Hold cleaning is preparation for cargo operations
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"HOLDS_PREPARATION": {
			ModifierUnlessUsed:            1.0, // Hold preparation is part of cargo operations
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"RIGGING": {
			ModifierUnlessUsed:            1.0, // Equipment rigging is preparation work
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"MOORING": {
			ModifierUnlessUsed:            1.0, // Mooring is vessel positioning for operations
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"OPENING_HOLDS": {
			ModifierUnlessUsed:            1.0, // Opening holds is part of cargo operations
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"CLOSING_HOLDS": {
			ModifierUnlessUsed:            1.0, // Closing holds is part of cargo operations
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
	}

	for k, v := range operationalPreparations {
		configs[k] = v
	}
}

// addCargoSpecificOperations adds cargo-specific operation stoppage configurations.
func addCargoSpecificOperations(configs map[string]model.StoppageConfiguration) {
	cargoSpecificOperations := map[string]model.StoppageConfiguration{
		"LOADING": {
			ModifierUnlessUsed:            1.0, // Loading is the primary cargo operation
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"DISCHARGING": {
			ModifierUnlessUsed:            1.0, // Discharging is the primary cargo operation
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"LOADING_STOPPAGE": {
			ModifierUnlessUsed:            1.0, // Loading stoppage is part of operations
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"DISCHARGING_STOPPAGE": {
			ModifierUnlessUsed:            1.0, // Discharging stoppage is part of operations
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"CARGO_CALCULATIONS": {
			ModifierUnlessUsed:            1.0, // Cargo calculations are administrative
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"SAMPLING": {
			ModifierUnlessUsed:            1.0, // Cargo sampling is quality control
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"GAUGING": {
			ModifierUnlessUsed:            1.0, // Cargo gauging is measurement
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"DRAFT_SURVEY": {
			ModifierUnlessUsed:            1.0, // Draft surveys are measurement/documentation
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"INITIAL_DRAFT_SURVEY": {
			ModifierUnlessUsed:            1.0, // Initial draft survey is documentation
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"FINAL_DRAFT_SURVEY": {
			ModifierUnlessUsed:            1.0, // Final draft survey is documentation
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
	}

	for k, v := range cargoSpecificOperations {
		configs[k] = v
	}
}

// addCargoWaitingPeriods adds waiting period cargo stoppage configurations.
func addCargoWaitingPeriods(configs map[string]model.StoppageConfiguration) {
	waitingPeriods := map[string]model.StoppageConfiguration{
		"WAITING_FOR_DAYLIGHT": {
			ModifierUnlessUsed:            1.0, // Waiting for daylight is normal scheduling
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"WAITING_FOR_TIDE": {
			ModifierUnlessUsed:            1.0, // Waiting for tide is normal scheduling
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
		"TIDE_RESTRICTION": {
			ModifierUnlessUsed:            1.0, // Tide restrictions are normal operational constraints
			ModifierNotUsed:               0.0,
			ModifierUnlessUsedOnDemurrage: toPtr(1.0),
			ModifierNotUsedOnDemurrage:    toPtr(1.0),
		},
	}

	for k, v := range waitingPeriods {
		configs[k] = v
	}
}
