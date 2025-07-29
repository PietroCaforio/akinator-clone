# akinator-clone

### Requirements
This project uses **Conda** for environment management.

To set up everything:

```bash
make deps      # Create the Conda environment
make data      # Download the dataset
```

#### To start the backend:
```bash
uvicorn backend.main:app --reload
```

### To setup and start the frontend:
```bash
cd akinator-frontend
npm install
npm run dev
```
