import discord
from discord.ext import commands
import os
import random
import requests
from discord.ui import Button, View

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Conectado como {bot.user}")

@bot.command()
async def meme(ctx):
    imagenes = os.listdir("imagenes")
    imagen_aleatoria = random.choice(imagenes)

    with open(f"imagenes/{imagen_aleatoria}", "rb") as f:
        imagen = discord.File(f)
    await ctx.send(file=imagen)

@bot.command()
async def meme_animales(ctx):
    animales = os.listdir("animales")
    imagen_aleatoria = random.choice(animales)

    with open(f"animales/{imagen_aleatoria}", "rb") as f:
        imagen = discord.File(f)
    await ctx.send(file=imagen)

#Imagenes de una pagina web

def obtener_zorro():
    url = "https://randomfox.ca/floof/"
    respuesta = requests.get(url)
    datos = respuesta.json()
    
    if "image" in datos:
        return datos["image"]
    elif "url" in datos:
        return datos["url"]
    else:
        return None

@bot.command()
async def zorro(ctx):
    url_imagen = obtener_zorro()
    if url_imagen:
        await ctx.send(url_imagen)
    else:
        await ctx.send("😕 No se pudo obtener la imagen del zorro. Intenta más tarde.")


def obtener_perro():
    url = "https://random.dog/woof.json"
    respuesta = requests.get(url)
    datos = respuesta.json()
    return datos ["url"]

@bot.command()
async def perro(ctx):
    url_imagen= obtener_perro()
    await ctx.send(url_imagen)

def obtener_pato():
    url = "https://random-d.uk/api/random"
    respuesta = requests.get(url)
    datos = respuesta.json()
    return datos ["url"]

@bot.command()
async def pato(ctx):
    url_imagen= obtener_pato()
    await ctx.send(url_imagen)



@bot.command()
async def hola(ctx):
    button = Button(label="¡Haz clic aquí!", style=discord.ButtonStyle.green)

    async def on_click(interaction):
        await interaction.response.send_message("¡Hola! 👋", ephemeral=True)

    button.callback = on_click
    view = View()
    view.add_item(button)
    
    await ctx.send(f"¡Hola! Soy un bot llamado {bot.user}. ¿Quieres que te salude?", view=view)

@bot.command()
async def say(ctx, *, mensaje):
    await ctx.send(f"{mensaje}")

@bot.command()
async def menu(ctx):
    embed = discord.Embed(
        title="📋 Menú de comandos",
        description="Aquí están los comandos disponibles(!):",
        color=discord.Color.blurple()
    )
    embed.add_field(name="`hola`", value="Saludo interactivo con botón.", inline=False)
    embed.add_field(name="`say <mensaje>`", value="Repite el mensaje que escribas.", inline=False)
    embed.add_field(name="`pato`", value="Muestra una imagen de un pato.", inline=False)
    embed.add_field(name="`meme`", value="Muestra un meme aleatorio.", inline=False)
    embed.add_field(name="`menu`", value="Muestra este menú de ayuda.", inline=False)
    embed.add_field(name="`perro`", value="Muestra una imagen de un perro.", inline=False)
    embed.add_field(name="`zorro`", value="Muestra una imagen de un zorro.", inline=False)

    await ctx.send(embed=embed)

bot.run("MTM4OTc2OTgzNDI5MTc4OTkzNQ.Gq1wAK.EJVYYtCplasiaD-uzUCdunGWSbAjcu9D0GKq4I")
