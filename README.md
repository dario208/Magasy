# MAGASY

## Description

Ce projet est une application de gestion de stock ou de site e-commerce permettant :
- De gérer les produits, les catégories et les commandes.
- D’assurer le suivi des stocks en temps réel, facilitant l’optimisation de l'inventaire.
- De proposer une expérience utilisateur simple et efficace pour la vente en ligne, si utilisé en mode e-commerce.

L'application est construite avec une architecture back-end et front-end séparée pour une flexibilité maximale.

## Fonctionnalités

1. **Gestion des produits** : Ajouter, modifier et supprimer des produits.
2. **Catégorisation des produits** : Organiser les produits par catégories.
3. **Suivi de stock** : Consulter les niveaux de stock, notifications de faible inventaire.
4. **Gestion des commandes** : Enregistrer et suivre les commandes clients (mode e-commerce).
5. **Interface utilisateur** : Interface intuitive pour l'administration ou pour la vente en ligne.

## Technologies utilisées

- **Backend** : FastAPI (API REST), SQLAlchemy (gestion des données)
- **Frontend** : React.js
- **Base de données** : PostgreSQL 
- **Gestion de conteneurs** : Docker et Docker Compose pour faciliter le déploiement
- **Authentification** : JWT ou OAuth pour sécuriser l'accès

## Installation

### Prérequis
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/)

### Étapes d'installation

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/ton-utilisateur/nom-du-projet.git
   cd nom-du-projet
