# Despliegue de Escritorios Virtuales en Huawei Cloud Workspace

Este proyecto contiene un script de Python que utiliza el SDK de Huawei Cloud para desplegar múltiples escritorios virtuales en el servicio Workspace. Los nombres de los escritorios a desplegar deben ser definidos en el arreglo `arrDesktop` dentro del código.

## 📌 Requisitos Previos

Antes de ejecutar el script, asegúrate de cumplir con los siguientes requisitos:

1. Tener instalado **Python 3.8 o superior**.
2. Contar con una cuenta en **Huawei Cloud** con los permisos necesarios para desplegar escritorios en Workspace.
3. Instalar `pip`, si aún no lo tienes instalado.
4. Tener acceso al **ID de Proyecto**, **Enterprise Project ID**, **Security Group**, **Subnet ID**, e **Image ID** necesarios para la configuración.
5. Contar con las credenciales de Huawei Cloud (`Access Key` y `Secret Key`).

## 🔧 Instalación de Dependencias

### 1️⃣ Instalar Python
Si aún no tienes Python instalado, descárgalo desde [python.org](https://www.python.org/downloads/) e instálalo siguiendo las instrucciones para tu sistema operativo.

Verifica la instalación ejecutando:

```sh
python --version
```

### 2️⃣ Instalar `pip`
Si `pip` no está instalado, puedes instalarlo con:

```sh
python -m ensurepip --default-pip
```

Asegúrate de actualizar `pip`:

```sh
python -m pip install --upgrade pip
```

### 3️⃣ Crear un Entorno Virtual (Opcional pero Recomendado)
Es recomendable trabajar dentro de un entorno virtual para evitar conflictos de dependencias:

```sh
python -m venv venv
source venv/bin/activate  # Para Linux/macOS
venv\Scripts\activate  # Para Windows
```

### 4️⃣ Instalar Jupyter Notebook (Opcional)
Si deseas ejecutar el script en Jupyter Notebook, instala Jupyter con:

```sh
pip install jupyter
```

Para abrir Jupyter Notebook:

```sh
jupyter notebook
```

### 5️⃣ Instalar Dependencias del Proyecto

Ejecuta el siguiente comando para instalar las librerías necesarias:

```sh
pip install python-dotenv huaweicloudsdkall
```

- **`python-dotenv`**: Permite cargar variables de entorno desde un archivo `.env`.
- **`huaweicloudsdkall`**: SDK de Huawei Cloud para interactuar con los servicios.

## 📂 Configuración del Archivo `.env`

Debes crear un archivo llamado `.env` en la raíz del proyecto y agregar las siguientes variables con sus respectivos valores:

```ini
CLOUD_SDK_AK = <Clave de acceso>
CLOUD_SDK_SK = <Clave secreta>
CLOUD_SDK_PROJECT_ID = <ID del Proyecto de la región>
CLOUD_SDK_REGION = <Región cloud, Si es Santiago usar la-south-2>
CLOUD_SDK_ENTERPRISEPROJECTID = <ID del Enterprise Project>
CLOUD_SDK_SECURITYGROUP = <ID del Security Group con nombre WorkspaceUserSecurityGroup>
CLOUD_SDK_SUBNETID = <ID de la subnet a desplegar>
CLOUD_SDK_IMAGEID = <ID de la imagen a desplegar>
```

📌 **Importante:** No compartas este archivo ni lo subas a GitHub, ya que contiene información sensible.

## 📝 Uso del Script

1. **Edita el script** y añade los nombres de los escritorios a desplegar en la variable `arrDesktop`:

```python
arrDesktop = ["Desktop1", "Desktop2", "Desktop3"]
```

2. **Ejecuta el script**:

Ejecutar todas las celdas de código del archivo Notebook.ipynb

3. El script se encargará de desplegar los escritorios definidos en `arrDesktop` en Huawei Cloud Workspace.

## 📌 Consideraciones Adicionales

- Si tienes errores relacionados con las credenciales, revisa que el archivo `.env` esté correctamente configurado.
- Si no tienes acceso a ciertos recursos, verifica los permisos de tu cuenta en Huawei Cloud.
- Puedes verificar el estado de los escritorios en la consola de [Huawei Cloud Workspace](https://console.huaweicloud.com/workspace/).



---

✨ ¡Gracias por usar este script! Si tienes preguntas, abre un issue en GitHub. 🚀
