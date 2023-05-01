import disnake

all_colour_roles = (
    1102654728757858379, 1102654728757858378, 1102654728757858377,
    1102654728757858376, 1102654728757858375, 1102654728757858374,
    1102654728741060697, 1102654728741060696, 1102654728741060695,
    1102654728741060694, 1102654728741060693, 1102654728741060692,
    1102654728741060691, 1102654728741060690, 1102654728741060689,
    1102654728741060688, 1102654728741060690, 1102654728720097378,
    1102654728720097377, 1102654728720097376  # The last one is owner only red
)

colour_roles = {
    'vystalia:colour_roles:Madang': 1102654728757858379, 'vystalia:colour_roles:Orchid': 1102654728757858378,
    'vystalia:colour_roles:Primrose': 1102654728757858377, 'vystalia:colour_roles:Ice_Cold': 1102654728757858376,
    'vystalia:colour_roles:Perano': 1102654728757858375, 'vystalia:colour_roles:Perfume': 1102654728757858374,
    'vystalia:colour_roles:Wewak': 1102654728741060697, 'vystalia:colour_roles:Illusion': 1102654728741060696,
    'vystalia:colour_roles:Mandys_Pink': 1102654728741060695, 'vystalia:colour_roles:White': 1102654728741060694,
    'vystalia:colour_roles:Black': 1102654728741060693, 'vystalia:colour_roles:Electric_Violet': 1102654728741060692,
    'vystalia:colour_roles:Broom': 1102654728741060691, 'vystalia:colour_roles:Screaming_Green': 1102654728741060690,
    'vystalia:colour_roles:Red_Orange': 1102654728741060689, 'vystalia:colour_roles:Dodger_Blue': 1102654728741060688,
    'vystalia:colour_roles:Spring_Green': 1102654728741060690, 'vystalia:colour_roles:Turquoise': 1102654728720097378,
    'vystalia:colour_roles:Sunshade': 1102654728720097377
}

__all__ = (
    'ColourButtonRoles',
    'all_colour_roles',
)


class ColourButtonRoles(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(label='Illusion', custom_id='vystalia:colour_roles:Illusion', emoji='<:illusion:938412173846270004>')
    async def Illusion(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        _roles = [role for role in interaction.author.roles if role.id not in all_colour_roles]
        _roles.append(interaction.guild.get_role(colour_roles[button.custom_id]))
        await interaction.author.edit(roles=_roles, reason='Colour role update.')
        await interaction.response.send_message(f'I have changed your colour to `{button.label}`', ephemeral=True)

    @disnake.ui.button(label='Black', custom_id='vystalia:colour_roles:Black', emoji='<:black:938412174785785886>')
    async def Black(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        _roles = [role for role in interaction.author.roles if role.id not in all_colour_roles]
        _roles.append(interaction.guild.get_role(colour_roles[button.custom_id]))
        await interaction.author.edit(roles=_roles, reason='Colour role update.')
        await interaction.response.send_message(f'I have changed your colour to `{button.label}`', ephemeral=True)

    @disnake.ui.button(label='Screaming Green', custom_id='vystalia:colour_roles:Screaming_Green', emoji='<:screaming_green:938412175763050547>')
    async def Screaming_Green(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        _roles = [role for role in interaction.author.roles if role.id not in all_colour_roles]
        _roles.append(interaction.guild.get_role(colour_roles[button.custom_id]))
        await interaction.author.edit(roles=_roles, reason='Colour role update.')
        await interaction.response.send_message(f'I have changed your colour to `{button.label}`', ephemeral=True)

    @disnake.ui.button(label='Electric Violet', custom_id='vystalia:colour_roles:Electric_Violet', emoji='<:electric_violet:938412176723558431>')
    async def Electric_Violet(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        _roles = [role for role in interaction.author.roles if role.id not in all_colour_roles]
        _roles.append(interaction.guild.get_role(colour_roles[button.custom_id]))
        await interaction.author.edit(roles=_roles, reason='Colour role update.')
        await interaction.response.send_message(f'I have changed your colour to `{button.label}`', ephemeral=True)

    @disnake.ui.button(label='Red Orange', custom_id='vystalia:colour_roles:Red_Orange', emoji='<:red_orange:938412177944088647>')
    async def Red_Orange(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        _roles = [role for role in interaction.author.roles if role.id not in all_colour_roles]
        _roles.append(interaction.guild.get_role(colour_roles[button.custom_id]))
        await interaction.author.edit(roles=_roles, reason='Colour role update.')
        await interaction.response.send_message(f'I have changed your colour to `{button.label}`', ephemeral=True)

    @disnake.ui.button(label='Dodger Blue', custom_id='vystalia:colour_roles:Dodger_Blue', emoji='<:dodger_blue:938412178808135720>')
    async def Dodger_Blue(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        _roles = [role for role in interaction.author.roles if role.id not in all_colour_roles]
        _roles.append(interaction.guild.get_role(colour_roles[button.custom_id]))
        await interaction.author.edit(roles=_roles, reason='Colour role update.')
        await interaction.response.send_message(f'I have changed your colour to `{button.label}`', ephemeral=True)

    @disnake.ui.button(label='Spring Green', custom_id='vystalia:colour_roles:Spring_Green', emoji='<:spring_green:938412179290460191>')
    async def Spring_Green(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        _roles = [role for role in interaction.author.roles if role.id not in all_colour_roles]
        _roles.append(interaction.guild.get_role(colour_roles[button.custom_id]))
        await interaction.author.edit(roles=_roles, reason='Colour role update.')
        await interaction.response.send_message(f'I have changed your colour to `{button.label}`', ephemeral=True)

    @disnake.ui.button(label='Madang', custom_id='vystalia:colour_roles:Madang', emoji='<:madang:938412180511006720>')
    async def Madang(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        _roles = [role for role in interaction.author.roles if role.id not in all_colour_roles]
        _roles.append(interaction.guild.get_role(colour_roles[button.custom_id]))
        await interaction.author.edit(roles=_roles, reason='Colour role update.')
        await interaction.response.send_message(f'I have changed your colour to `{button.label}`', ephemeral=True)

    @disnake.ui.button(label='Perfume', custom_id='vystalia:colour_roles:Perfume', emoji='<:perfume:938412181534437446>')
    async def Perfume(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        _roles = [role for role in interaction.author.roles if role.id not in all_colour_roles]
        _roles.append(interaction.guild.get_role(colour_roles[button.custom_id]))
        await interaction.author.edit(roles=_roles, reason='Colour role update.')
        await interaction.response.send_message(f'I have changed your colour to `{button.label}`', ephemeral=True)

    @disnake.ui.button(label='Ice Cold', custom_id='vystalia:colour_roles:Ice_Cold', emoji='<:ice_cold:938412182411034654>')
    async def Ice_Cold(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        _roles = [role for role in interaction.author.roles if role.id not in all_colour_roles]
        _roles.append(interaction.guild.get_role(colour_roles[button.custom_id]))
        await interaction.author.edit(roles=_roles, reason='Colour role update.')
        await interaction.response.send_message(f'I have changed your colour to `{button.label}`', ephemeral=True)

    @disnake.ui.button(label='Primrose', custom_id='vystalia:colour_roles:Primrose', emoji='<:primrose:938412183262478377>')
    async def Primrose(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        _roles = [role for role in interaction.author.roles if role.id not in all_colour_roles]
        _roles.append(interaction.guild.get_role(colour_roles[button.custom_id]))
        await interaction.author.edit(roles=_roles, reason='Colour role update.')
        await interaction.response.send_message(f'I have changed your colour to `{button.label}`', ephemeral=True)

    @disnake.ui.button(label='Orchid', custom_id='vystalia:colour_roles:Orchid', emoji='<:orchid:938412192196350003>')
    async def Orchid(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        _roles = [role for role in interaction.author.roles if role.id not in all_colour_roles]
        _roles.append(interaction.guild.get_role(colour_roles[button.custom_id]))
        await interaction.author.edit(roles=_roles, reason='Colour role update.')
        await interaction.response.send_message(f'I have changed your colour to `{button.label}`', ephemeral=True)

    @disnake.ui.button(label='Mandys Pink', custom_id='vystalia:colour_roles:Mandys_Pink', emoji='<:mandys_pink:938412184302657566>')
    async def Mandys_Pink(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        _roles = [role for role in interaction.author.roles if role.id not in all_colour_roles]
        _roles.append(interaction.guild.get_role(colour_roles[button.custom_id]))
        await interaction.author.edit(roles=_roles, reason='Colour role update.')
        await interaction.response.send_message(f'I have changed your colour to `{button.label}`', ephemeral=True)

    @disnake.ui.button(label='Perano', custom_id='vystalia:colour_roles:Perano', emoji='<:perano:938412185762291812>')
    async def Perano(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        _roles = [role for role in interaction.author.roles if role.id not in all_colour_roles]
        _roles.append(interaction.guild.get_role(colour_roles[button.custom_id]))
        await interaction.author.edit(roles=_roles, reason='Colour role update.')
        await interaction.response.send_message(f'I have changed your colour to `{button.label}`', ephemeral=True)

    @disnake.ui.button(label='Turquoise', custom_id='vystalia:colour_roles:Turquoise', emoji='<:turquoise:938412186924109874>')
    async def Turquoise(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        _roles = [role for role in interaction.author.roles if role.id not in all_colour_roles]
        _roles.append(interaction.guild.get_role(colour_roles[button.custom_id]))
        await interaction.author.edit(roles=_roles, reason='Colour role update.')
        await interaction.response.send_message(f'I have changed your colour to `{button.label}`', ephemeral=True)

    @disnake.ui.button(label='Wewak', custom_id='vystalia:colour_roles:Wewak', emoji='<:wewak:938412188165632010>')
    async def Wewak(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        _roles = [role for role in interaction.author.roles if role.id not in all_colour_roles]
        _roles.append(interaction.guild.get_role(colour_roles[button.custom_id]))
        await interaction.author.edit(roles=_roles, reason='Colour role update.')
        await interaction.response.send_message(f'I have changed your colour to `{button.label}`', ephemeral=True)

    @disnake.ui.button(label='Sunshade', custom_id='vystalia:colour_roles:Sunshade', emoji='<:sunshade:938412189172265050>')
    async def Sunshade(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        _roles = [role for role in interaction.author.roles if role.id not in all_colour_roles]
        _roles.append(interaction.guild.get_role(colour_roles[button.custom_id]))
        await interaction.author.edit(roles=_roles, reason='Colour role update.')
        await interaction.response.send_message(f'I have changed your colour to `{button.label}`', ephemeral=True)

    @disnake.ui.button(label='White', custom_id='vystalia:colour_roles:White', emoji='<:white:886669988558176306>')
    async def White(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        _roles = [role for role in interaction.author.roles if role.id not in all_colour_roles]
        _roles.append(interaction.guild.get_role(colour_roles[button.custom_id]))
        await interaction.author.edit(roles=_roles, reason='Colour role update.')
        await interaction.response.send_message(f'I have changed your colour to `{button.label}`', ephemeral=True)

    @disnake.ui.button(label='Broom', custom_id='vystalia:colour_roles:Broom', emoji='<:broom:938412190996774974>')
    async def Broom(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        _roles = [role for role in interaction.author.roles if role.id not in all_colour_roles]
        _roles.append(interaction.guild.get_role(colour_roles[button.custom_id]))
        await interaction.author.edit(roles=_roles, reason='Colour role update.')
        await interaction.response.send_message(f'I have changed your colour to `{button.label}`', ephemeral=True)
