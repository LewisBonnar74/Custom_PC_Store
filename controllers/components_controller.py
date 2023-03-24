from flask import Flask, render_template, request, redirect
from repositories import component_repository
from repositories import custom_pc_repository
from models.custom_pc import Custom_pc
from models.component import Component

from flask import Blueprint

components_blueprint = Blueprint("components", __name__)
