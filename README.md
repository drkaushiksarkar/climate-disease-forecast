# climate-disease-forecast

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![ERA5](https://img.shields.io/badge/ERA5-Reanalysis-4E9BCD?style=flat-square)
![Agents](https://img.shields.io/badge/Agentic_AI-FF6F00?style=flat-square)

Climate-driven disease prediction with agent-based ensemble modeling, ERA5 reanalysis integration, and uncertainty-quantified forecasting.

---

## Architecture

```
ERA5 Reanalysis          Disease Surveillance         Population Data
(temperature,            (incidence rates,            (demographics,
 precipitation,           case counts,                 mobility)
 humidity, wind)          mortality)
        |                       |                          |
        +----------+------------+--------------------------+
                   |
          DataAcquisitionAgent
          (fetch, validate, gap-fill, merge)
                   |
          EnsembleRoutingAgent
          (model selection, weight assignment, BMA)
                   |
     +-------------+-------------+-------------+
     |             |             |             |
   ARIMA       Prophet       XGBoost       LSTM
     |             |             |             |
     +-------------+-------------+-------------+
                   |
          Bayesian Model Averaging
          (uncertainty quantification)
                   |
          Prediction Output
          (mean, CI_lower, CI_upper)
```

## Agent system

The `agents/` package implements autonomous model ensemble routing:

- **EnsembleRoutingAgent** -- Dynamically selects and weights forecast models based on recent accuracy. Maintains a model registry with performance tracking and produces uncertainty-quantified predictions through Bayesian model averaging.

- **DataAcquisitionAgent** -- Autonomously fetches and validates climate data from ERA5 reanalysis. Quality checks for missing values, outliers, and temporal continuity with automated gap filling.

## Data sources

| Source | Variables | Resolution |
|:-------|:----------|:-----------|
| ERA5 reanalysis | Temperature, precipitation, humidity, wind, pressure | 0.25 degree, monthly |
| WHO GHO | Disease incidence and mortality rates | Country-level, annual |
| National HMIS | Subnational case counts and sentinel surveillance | District-level, weekly/monthly |
| WorldPop | Population density and demographics | 1km grid, annual |

## Components

| Module | Purpose |
|:-------|:--------|
| `agents/ensemble_agent.py` | Autonomous model selection and ensemble routing |
| `agents/__init__.py` | Agent package exports |
| `models/` | Individual forecast model implementations |
| `data/` | Data loading, preprocessing, and feature engineering |
| `evaluation/` | Forecast verification and skill scoring |

## Quick start

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Run ensemble forecast
python -m agents.ensemble_agent --country BGD --indicator malaria_incidence --horizon 6
```

## License

MIT
