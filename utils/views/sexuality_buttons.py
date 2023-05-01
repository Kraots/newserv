import disnake

all_sexuality_roles = (
    1102654728699117574, 1102654728699117573, 1102654728699117572,
    1102654728699117571, 1102654728699117570, 1102654728699117569,
    1102654728350998547
)

sexuality_roles = {
    'vystalia:sexuality_roles:Straight': 1102654728699117574, 'vystalia:sexuality_roles:Bisexual': 1102654728699117573,
    'vystalia:sexuality_roles:Gay': 1102654728699117572, 'vystalia:sexuality_roles:Lesbian': 1102654728699117571,
    'vystalia:sexuality_roles:Asexual': 1102654728699117570, 'vystalia:sexuality_roles:Queer': 1102654728699117569,
    'vystalia:sexuality_roles:Other-Sexuality': 1102654728350998547
}

__all__ = (
    'SexualityButtonRoles',
    'all_sexuality_roles',
)


class SexualityButtonRoles(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(label='Straight', custom_id='vystalia:sexuality_roles:Straight', row=0, style=disnake.ButtonStyle.blurple)
    async def Straight(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        roles = [role for role in interaction.author.roles if role.id not in all_sexuality_roles]
        roles.append(interaction.guild.get_role(sexuality_roles[button.custom_id]))
        await interaction.author.edit(roles=roles, reason='Sexuality role update.')
        await interaction.response.send_message(f'I have changed your sexuality role to `{button.label}`', ephemeral=True)

    @disnake.ui.button(label='Gay', custom_id='vystalia:sexuality_roles:Gay', row=0, style=disnake.ButtonStyle.blurple)
    async def Gay(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        roles = [role for role in interaction.author.roles if role.id not in all_sexuality_roles]
        roles.append(interaction.guild.get_role(sexuality_roles[button.custom_id]))
        await interaction.author.edit(roles=roles, reason='Sexuality role update.')
        await interaction.response.send_message(f'I have changed your sexuality role to `{button.label}`', ephemeral=True)

    @disnake.ui.button(label='Lesbian', custom_id='vystalia:sexuality_roles:Lesbian', row=0, style=disnake.ButtonStyle.blurple)
    async def Lesbian(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        roles = [role for role in interaction.author.roles if role.id not in all_sexuality_roles]
        roles.append(interaction.guild.get_role(sexuality_roles[button.custom_id]))
        await interaction.author.edit(roles=roles, reason='Sexuality role update.')
        await interaction.response.send_message(f'I have changed your sexuality role to `{button.label}`', ephemeral=True)

    @disnake.ui.button(label='Bisexual', custom_id='vystalia:sexuality_roles:Bisexual', row=1, style=disnake.ButtonStyle.blurple)
    async def Bisexual(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        roles = [role for role in interaction.author.roles if role.id not in all_sexuality_roles]
        roles.append(interaction.guild.get_role(sexuality_roles[button.custom_id]))
        await interaction.author.edit(roles=roles, reason='Sexuality role update.')
        await interaction.response.send_message(f'I have changed your sexuality role to `{button.label}`', ephemeral=True)

    @disnake.ui.button(label='Asexual', custom_id='vystalia:sexuality_roles:Asexual', row=1, style=disnake.ButtonStyle.blurple)
    async def Asexual(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        roles = [role for role in interaction.author.roles if role.id not in all_sexuality_roles]
        roles.append(interaction.guild.get_role(sexuality_roles[button.custom_id]))
        await interaction.author.edit(roles=roles, reason='Sexuality role update.')
        await interaction.response.send_message(f'I have changed your sexuality role to `{button.label}`', ephemeral=True)

    @disnake.ui.button(label='Queer', custom_id='vystalia:sexuality_roles:Queer', row=1, style=disnake.ButtonStyle.blurple)
    async def Queer(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        roles = [role for role in interaction.author.roles if role.id not in all_sexuality_roles]
        roles.append(interaction.guild.get_role(sexuality_roles[button.custom_id]))
        await interaction.author.edit(roles=roles, reason='Sexuality role update.')
        await interaction.response.send_message(f'I have changed your sexuality role to `{button.label}`', ephemeral=True)

    @disnake.ui.button(label='Other Sexuality', custom_id='vystalia:sexuality_roles:Other-Sexuality', row=2, style=disnake.ButtonStyle.blurple)
    async def Other_Sexuality(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        roles = [role for role in interaction.author.roles if role.id not in all_sexuality_roles]
        roles.append(interaction.guild.get_role(sexuality_roles[button.custom_id]))
        await interaction.author.edit(roles=roles, reason='Sexuality role update.')
        await interaction.response.send_message(f'I have changed your sexuality role to `{button.label}`', ephemeral=True)
